# Day 0: Linux Fundamentals - Complete 8-Hour Plan

## 🎯 Today's Mission

Master the Linux command line - the foundation of every DevOps skill you'll learn. By the end of today, you'll be comfortable navigating, managing, and troubleshooting Linux systems.

## 📋 Prerequisites

- Terminal access (macOS Terminal, Linux Terminal, or WSL2 on Windows)
- Ubuntu/Debian system recommended (or macOS with minor differences)
- Text editor (nano, vim, or VS Code)
- Root/sudo access

## ⏰ 8-Hour Learning Schedule

---

### Hour 1: File System Navigation & Basic Operations (9:00 AM - 10:00 AM)

**Theory (15 minutes)**
- Linux file system hierarchy
  ```
  /           Root directory
  /home       User home directories
  /etc        Configuration files
  /var        Variable data (logs, cache)
  /tmp        Temporary files
  /usr        User programs
  /bin        Essential binaries
  /sbin       System binaries
  /opt        Optional software
  /dev        Device files
  /proc       Process information
  ```
- Understanding paths (absolute vs relative)
- File and directory concepts

**Hands-On Practice (45 minutes)**

1. **Navigation Basics**
   ```bash
   # Where am I?
   pwd
   
   # List files
   ls
   ls -l        # Long format
   ls -la       # Include hidden files
   ls -lh       # Human-readable sizes
   ls -ltr      # Sort by time, reversed
   
   # Change directory
   cd /
   cd /home
   cd ~         # Home directory
   cd ..        # Parent directory
   cd -         # Previous directory
   
   # Special directories
   .            # Current directory
   ..           # Parent directory
   ~            # Home directory
   -            # Previous directory
   ```

2. **File Operations**
   ```bash
   # Create files
   touch file1.txt
   touch file2.txt file3.txt
   
   # Create directories
   mkdir mydir
   mkdir -p parent/child/grandchild  # Create parent dirs
   
   # Copy files
   cp file1.txt file1_backup.txt
   cp -r mydir mydir_backup  # Copy directory
   
   # Move/rename
   mv file1.txt newname.txt
   mv newname.txt mydir/
   
   # Remove files
   rm file2.txt
   rm -f file3.txt           # Force remove
   rm -r mydir_backup        # Remove directory
   rm -rf dangerous/         # Force remove directory (CAREFUL!)
   
   # View file contents
   cat file1.txt             # Display entire file
   less /var/log/syslog      # Page through file
   head -n 10 file.txt       # First 10 lines
   tail -n 20 file.txt       # Last 20 lines
   tail -f /var/log/syslog   # Follow file (real-time)
   ```

3. **File Searching**
   ```bash
   # Find files by name
   find /home -name "*.txt"
   find . -type f -name "file*"
   find . -type d -name "dir*"
   
   # Find files by size
   find /var/log -size +100M
   
   # Find and execute
   find . -name "*.log" -exec rm {} \;
   
   # Locate (faster but uses database)
   updatedb                  # Update database
   locate filename
   ```

**Learning Check**
- [ ] Can navigate to any directory
- [ ] Create, copy, move, delete files and directories
- [ ] Find files using find and locate
- [ ] View file contents different ways

---

### Hour 2: File Permissions & Ownership (10:00 AM - 11:00 AM)

**Theory (20 minutes)**
- Permission types: Read (r), Write (w), Execute (x)
- Permission groups: Owner, Group, Others
- Numeric permissions (octal notation)
  ```
  r = 4, w = 2, x = 1
  rwx = 7, rw- = 6, r-x = 5, r-- = 4
  Example: 755 = rwxr-xr-x
  ```
- Special permissions: SUID, SGID, Sticky bit

**Hands-On Practice (40 minutes)**

1. **Understanding Permissions**
   ```bash
   # Create test file
   touch testfile.txt
   
   # View permissions
   ls -l testfile.txt
   # Output: -rw-r--r-- 1 user group 0 Feb 22 09:00 testfile.txt
   #         │││ │││ │││
   #         │││ │││ └── Others permissions
   #         │││ └────── Group permissions  
   #         └────────── Owner permissions
   
   # File type indicators
   -    # Regular file
   d    # Directory
   l    # Symbolic link
   b    # Block device
   c    # Character device
   ```

2. **Changing Permissions**
   ```bash
   # Symbolic method
   chmod u+x testfile.txt    # Add execute for owner
   chmod g+w testfile.txt    # Add write for group
   chmod o-r testfile.txt    # Remove read for others
   chmod a+x testfile.txt    # Add execute for all
   chmod u=rwx,g=rx,o=r testfile.txt
   
   # Numeric method
   chmod 755 testfile.txt    # rwxr-xr-x
   chmod 644 testfile.txt    # rw-r--r--
   chmod 700 testfile.txt    # rwx------
   chmod 777 testfile.txt    # rwxrwxrwx (AVOID in production!)
   
   # Recursive
   chmod -R 755 mydir/
   ```

3. **Changing Ownership**
   ```bash
   # Change owner
   sudo chown newuser testfile.txt
   
   # Change group
   sudo chgrp newgroup testfile.txt
   
   # Change both
   sudo chown newuser:newgroup testfile.txt
   
   # Recursive
   sudo chown -R user:group mydir/
   ```

4. **Special Permissions**
   ```bash
   # SUID (Set User ID) - Run as file owner
   chmod u+s file
   chmod 4755 file
   
   # SGID (Set Group ID) - Run as group owner
   chmod g+s file
   chmod 2755 file
   
   # Sticky Bit - Only owner can delete
   chmod +t directory
   chmod 1755 directory
   
   # Example: /tmp directory
   ls -ld /tmp
   # drwxrwxrwt  # Sticky bit set
   ```

5. **Default Permissions (umask)**
   ```bash
   # View current umask
   umask
   
   # Set umask
   umask 022    # Default: 755 for dirs, 644 for files
   umask 077    # Restrictive: 700 for dirs, 600 for files
   
   # Test it
   umask 022
   touch test1.txt
   ls -l test1.txt    # Should be 644
   ```

**Practice Exercise**
```bash
# Create a script file
echo '#!/bin/bash' > myscript.sh
echo 'echo "Hello World"' >> myscript.sh

# Make it executable
chmod +x myscript.sh

# Run it
./myscript.sh

# Set proper permissions
chmod 750 myscript.sh  # Owner can do everything, group can read/execute
```

**Learning Check**
- [ ] Understand rwx permissions
- [ ] Can use chmod with both symbolic and numeric notation
- [ ] Can change file ownership
- [ ] Understand umask concept

---

### Hour 3: Text Processing & Filters (11:00 AM - 12:00 PM)

**Theory (10 minutes)**
- UNIX philosophy: Small tools that do one thing well
- Pipes and redirection
- Stream processing

**Hands-On Practice (50 minutes)**

1. **Basic Text Tools**
   ```bash
   # Create sample file
   cat > sample.txt << EOF
   John,25,Developer
   Jane,30,Manager
   Bob,28,Designer
   Alice,35,Developer
   Charlie,22,Intern
   EOF
   
   # View file
   cat sample.txt
   less sample.txt
   more sample.txt
   
   # Count lines, words, characters
   wc sample.txt
   wc -l sample.txt    # Lines only
   wc -w sample.txt    # Words only
   wc -c sample.txt    # Characters only
   ```

2. **Grep - Pattern Searching**
   ```bash
   # Basic search
   grep "Developer" sample.txt
   
   # Case-insensitive
   grep -i "developer" sample.txt
   
   # Show line numbers
   grep -n "Developer" sample.txt
   
   # Invert match (show non-matching lines)
   grep -v "Developer" sample.txt
   
   # Count matches
   grep -c "Developer" sample.txt
   
   # Recursive search in directory
   grep -r "TODO" /path/to/project
   
   # Extended regex
   grep -E "Developer|Manager" sample.txt
   
   # Practical: Search logs
   grep "ERROR" /var/log/syslog
   grep -i "failed" /var/log/auth.log
   ```

3. **Sed - Stream Editor**
   ```bash
   # Substitute text
   sed 's/Developer/Engineer/' sample.txt
   sed 's/Developer/Engineer/g' sample.txt  # Global (all occurrences)
   
   # In-place editing
   sed -i 's/Developer/Engineer/g' sample.txt
   
   # Delete lines
   sed '/Intern/d' sample.txt    # Delete lines with "Intern"
   sed '2d' sample.txt            # Delete line 2
   sed '2,4d' sample.txt          # Delete lines 2-4
   
   # Print specific lines
   sed -n '2,3p' sample.txt       # Print lines 2-3
   
   # Multiple commands
   sed -e 's/Developer/Engineer/' -e 's/Manager/Lead/' sample.txt
   ```

4. **Awk - Text Processing**
   ```bash
   # Print columns
   awk -F',' '{print $1}' sample.txt           # First column (name)
   awk -F',' '{print $1, $2}' sample.txt       # Name and age
   awk -F',' '{print $3}' sample.txt           # Role
   
   # With conditions
   awk -F',' '$2 > 25 {print $1}' sample.txt   # Names where age > 25
   awk -F',' '$3 == "Developer" {print $1}' sample.txt
   
   # Calculations
   awk -F',' '{sum+=$2} END {print sum}' sample.txt      # Sum of ages
   awk -F',' '{sum+=$2} END {print sum/NR}' sample.txt   # Average age
   
   # Format output
   awk -F',' '{printf "%-10s %d\n", $1, $2}' sample.txt
   ```

5. **Cut, Sort, Uniq**
   ```bash
   # Cut columns
   cut -d',' -f1 sample.txt      # First field
   cut -d',' -f1,3 sample.txt    # Fields 1 and 3
   
   # Sort
   sort sample.txt
   sort -r sample.txt             # Reverse
   sort -n sample.txt             # Numeric sort
   sort -t',' -k2 -n sample.txt   # Sort by 2nd column numerically
   
   # Unique lines
   sort sample.txt | uniq
   sort sample.txt | uniq -c      # Count occurrences
   sort sample.txt | uniq -d      # Show only duplicates
   ```

6. **Pipes and Redirection**
   ```bash
   # Output redirection
   ls -l > file_list.txt          # Overwrite
   ls -l >> file_list.txt         # Append
   
   # Input redirection
   wc -l < sample.txt
   
   # Pipes
   cat sample.txt | grep "Developer"
   cat sample.txt | grep "Developer" | wc -l
   
   # Complex pipeline
   cat /var/log/syslog | grep "error" | awk '{print $5}' | sort | uniq -c
   
   # Redirect stderr
   command 2> errors.txt
   command > output.txt 2>&1      # Redirect both stdout and stderr
   command &> all_output.txt      # Short form
   ```

**Real-World Example: Log Analysis**
```bash
# Find top 10 IP addresses in access log
cat access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -10

# Count HTTP status codes
cat access.log | awk '{print $9}' | sort | uniq -c

# Find errors in last hour
grep "$(date -d '1 hour ago' '+%d/%b/%Y:%H')" error.log | grep "ERROR"
```

**Learning Check**
- [ ] Can search text with grep
- [ ] Can modify text with sed
- [ ] Can process columns with awk
- [ ] Understand pipes and redirection
- [ ] Can build complex pipelines

---

### **LUNCH BREAK** (12:00 PM - 1:00 PM)

---

### Hour 4: Process Management (1:00 PM - 2:00 PM)

**Theory (15 minutes)**
- What is a process?
- Process states (running, sleeping, stopped, zombie)
- Process hierarchy (parent/child)
- Signals (SIGTERM, SIGKILL, SIGHUP, etc.)
- Foreground vs background processes

**Hands-On Practice (45 minutes)**

1. **Viewing Processes**
   ```bash
   # List all processes
   ps
   ps aux           # All processes, detailed
   ps -ef           # Full format
   
   # Process tree
   pstree
   ps auxf          # Forest view
   
   # Filter processes
   ps aux | grep nginx
   pgrep nginx      # Get PID by name
   pidof nginx      # Alternative
   
   # Real-time monitoring
   top              # Interactive process viewer
   # Press 'h' for help
   # Press 'k' to kill a process
   # Press 'M' to sort by memory
   # Press 'P' to sort by CPU
   # Press 'q' to quit
   
   # Better alternative
   htop             # Install if needed: sudo apt install htop
   ```

2. **Managing Processes**
   ```bash
   # Start background process
   sleep 100 &
   
   # List background jobs
   jobs
   
   # Bring to foreground
   fg %1
   
   # Send to background (Ctrl+Z first)
   bg %1
   
   # Disown (detach from terminal)
   sleep 1000 &
   disown
   ```

3. **Killing Processes**
   ```bash
   # Get process ID
   ps aux | grep sleep
   
   # Kill by PID (graceful)
   kill PID
   kill -15 PID      # SIGTERM (default)
   
   # Force kill
   kill -9 PID       # SIGKILL (cannot be caught)
   
   # Kill by name
   killall sleep
   pkill sleep
   
   # Kill all processes of a user
   pkill -u username
   
   # Common signals
   kill -l           # List all signals
   kill -1 PID       # SIGHUP (reload config)
   kill -2 PID       # SIGINT (Ctrl+C)
   kill -9 PID       # SIGKILL (force)
   kill -15 PID      # SIGTERM (graceful)
   ```

4. **Process Priority**
   ```bash
   # Nice values: -20 (highest) to 19 (lowest)
   
   # Start with lower priority
   nice -n 10 command
   
   # Change priority of running process
   renice -n 5 -p PID
   
   # View process priority
   ps -eo pid,comm,nice
   ```

5. **System Services (systemd)**
   ```bash
   # Check service status
   sudo systemctl status nginx
   sudo systemctl status ssh
   
   # Start/stop service
   sudo systemctl start nginx
   sudo systemctl stop nginx
   sudo systemctl restart nginx
   sudo systemctl reload nginx    # Reload config without restart
   
   # Enable/disable at boot
   sudo systemctl enable nginx
   sudo systemctl disable nginx
   
   # List all services
   sudo systemctl list-units --type=service
   sudo systemctl list-units --state=running
   sudo systemctl list-units --state=failed
   
   # View service logs
   sudo journalctl -u nginx
   sudo journalctl -u nginx -f     # Follow
   sudo journalctl -u nginx --since "1 hour ago"
   ```

**Practice Exercise: Process Monitoring Script**
```bash
#!/bin/bash
# monitor.sh - Monitor CPU and Memory usage

while true; do
    clear
    echo "=== System Monitor ==="
    echo "Date: $(date)"
    echo ""
    
    echo "Top 5 CPU consumers:"
    ps aux --sort=-%cpu | head -6
    echo ""
    
    echo "Top 5 Memory consumers:"
    ps aux --sort=-%mem | head -6
    echo ""
    
    echo "Load Average:"
    uptime
    
    sleep 5
done
```

**Learning Check**
- [ ] Can view and monitor processes
- [ ] Can kill processes properly
- [ ] Understand process signals
- [ ] Can manage system services
- [ ] Can use top/htop effectively

---

### Hour 5: User & Group Management (2:00 PM - 3:00 PM)

**Theory (15 minutes)**
- User types (root, system users, regular users)
- UID and GID concepts
- /etc/passwd, /etc/shadow, /etc/group files
- sudo and su differences

**Hands-On Practice (45 minutes)**

1. **User Information**
   ```bash
   # Current user
   whoami
   id
   
   # Logged in users
   who
   w
   last           # Login history
   
   # User details
   id username
   finger username
   
   # View user database files
   cat /etc/passwd
   cat /etc/group
   # Note: /etc/shadow requires sudo
   ```

2. **Creating Users**
   ```bash
   # Add user (basic)
   sudo useradd john
   
   # Add user with home directory
   sudo useradd -m jane
   
   # Add user with specific shell
   sudo useradd -m -s /bin/bash bob
   
   # Add user with specific UID
   sudo useradd -m -u 1500 alice
   
   # Add user with comment
   sudo useradd -m -c "Alice Developer" alice
   
   # Add user to specific group
   sudo useradd -m -g developers charlie
   
   # Complete example
   sudo useradd -m -s /bin/bash -c "John Doe" -G sudo,developers john
   
   # Set password
   sudo passwd john
   ```

3. **Modifying Users**
   ```bash
   # Change user shell
   sudo usermod -s /bin/zsh john
   
   # Add user to group
   sudo usermod -aG docker john
   sudo usermod -aG sudo john
   
   # Change home directory
   sudo usermod -d /new/home john
   
   # Lock/unlock user
   sudo usermod -L john    # Lock
   sudo usermod -U john    # Unlock
   
   # Change username
   sudo usermod -l newname oldname
   ```

4. **Deleting Users**
   ```bash
   # Delete user (keep home directory)
   sudo userdel john
   
   # Delete user and home directory
   sudo userdel -r john
   ```

5. **Group Management**
   ```bash
   # Create group
   sudo groupadd developers
   sudo groupadd -g 2000 devops    # Specific GID
   
   # Delete group
   sudo groupdel developers
   
   # Add user to group
   sudo gpasswd -a username groupname
   sudo usermod -aG groupname username
   
   # Remove user from group
   sudo gpasswd -d username groupname
   
   # List groups
   groups
   groups username
   
   # Change primary group
   sudo usermod -g groupname username
   ```

6. **Sudo and Su**
   ```bash
   # Switch user
   su username
   su -              # Switch to root with environment
   su - username     # Switch with user's environment
   
   # Exit back
   exit
   
   # Execute as another user
   sudo -u username command
   
   # Become root
   sudo -i           # Root shell with environment
   sudo -s           # Root shell, keep environment
   sudo su -         # Alternative
   
   # Edit sudoers file (ALWAYS use visudo!)
   sudo visudo
   
   # Grant sudo access
   # Add to /etc/sudoers:
   username ALL=(ALL:ALL) ALL
   
   # Passwordless sudo
   username ALL=(ALL) NOPASSWD: ALL
   
   # Specific command only
   username ALL=(ALL) NOPASSWD: /bin/systemctl restart nginx
   ```

**Practice Exercise: Multi-User Setup**
```bash
#!/bin/bash
# setup-dev-team.sh - Setup development team users

# Create group
sudo groupadd developers

# Create users
for user in alice bob charlie; do
    sudo useradd -m -s /bin/bash -G developers $user
    echo "$user:password123" | sudo chpasswd
    echo "Created user: $user"
done

# Create shared project directory
sudo mkdir -p /projects/team
sudo chgrp developers /projects/team
sudo chmod 775 /projects/team

echo "Team setup complete!"
```

**Learning Check**
- [ ] Can create and manage users
- [ ] Can manage groups
- [ ] Understand sudo vs su
- [ ] Can set proper permissions for multi-user environment
- [ ] Know how to edit sudoers safely

---

### Hour 6: Networking Basics (3:00 PM - 4:00 PM)

**Theory (15 minutes)**
- Network interfaces
- IP addressing (IPv4/IPv6)
- Ports and services
- Common protocols (HTTP, SSH, FTP, etc.)
- Firewall basics

**Hands-On Practice (45 minutes)**

1. **Network Interface Info**
   ```bash
   # View interfaces (old command)
   ifconfig
   
   # View interfaces (new command)
   ip addr show
   ip a          # Short form
   
   # Specific interface
   ip addr show eth0
   
   # Interface stats
   ip -s link
   
   # Bring interface up/down
   sudo ip link set eth0 down
   sudo ip link set eth0 up
   ```

2. **Network Configuration**
   ```bash
   # View routing table
   ip route show
   route -n
   
   # Add route
   sudo ip route add 192.168.1.0/24 via 192.168.0.1
   
   # Default gateway
   ip route show default
   
   # DNS configuration
   cat /etc/resolv.conf
   
   # Hostname
   hostname
   hostnamectl
   sudo hostnamectl set-hostname newhostname
   ```

3. **Network Testing**
   ```bash
   # Ping
   ping google.com
   ping -c 4 8.8.8.8         # 4 packets only
   
   # Traceroute
   traceroute google.com
   tracepath google.com
   
   # DNS lookup
   nslookup google.com
   dig google.com
   host google.com
   
   # Check connectivity
   nc -zv google.com 80      # Netcat port check
   telnet google.com 80
   ```

4. **Port and Service Info**
   ```bash
   # Active connections (old)
   netstat -tulpn
   # t = TCP, u = UDP, l = listening, p = program, n = numeric
   
   # Active connections (new)
   ss -tulpn
   ss -tunap          # All connections
   
   # Specific port
   ss -tunap | grep :80
   lsof -i :80        # Using lsof
   
   # All listening ports
   sudo netstat -plant | grep LISTEN
   sudo ss -tlnp
   ```

5. **File Transfer**
   ```bash
   # Download file
   wget https://example.com/file.txt
   wget -O renamed.txt https://example.com/file.txt
   
   # Better alternative
   curl -O https://example.com/file.txt
   curl -o renamed.txt https://example.com/file.txt
   
   # SCP (Secure Copy)
   scp file.txt user@remote:/path/
   scp user@remote:/path/file.txt ./
   scp -r directory/ user@remote:/path/
   
   # RSYNC (better for large transfers)
   rsync -avz source/ user@remote:/dest/
   rsync -avz --progress source/ dest/
   ```

6. **SSH**
   ```bash
   # Connect to remote server
   ssh user@hostname
   ssh user@192.168.1.10
   ssh -p 2222 user@hostname     # Custom port
   
   # Execute remote command
   ssh user@hostname 'ls -la'
   
   # SSH key generation
   ssh-keygen -t rsa -b 4096
   ssh-keygen -t ed25519
   
   # Copy SSH key to server
   ssh-copy-id user@hostname
   
   # SSH config file
   cat > ~/.ssh/config << EOF
   Host myserver
       HostName 192.168.1.10
       User john
       Port 22
       IdentityFile ~/.ssh/id_rsa
   EOF
   
   # Now connect simply
   ssh myserver
   ```

7. **Firewall (UFW)**
   ```bash
   # Install UFW
   sudo apt install ufw
   
   # Enable/disable
   sudo ufw enable
   sudo ufw disable
   
   # Status
   sudo ufw status
   sudo ufw status verbose
   
   # Allow service
   sudo ufw allow ssh
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   sudo ufw allow 3000:3100/tcp    # Port range
   
   # Allow from specific IP
   sudo ufw allow from 192.168.1.100
   sudo ufw allow from 192.168.1.0/24
   
   # Deny
   sudo ufw deny 23
   
   # Delete rule
   sudo ufw delete allow 80/tcp
   
   # Reset
   sudo ufw reset
   ```

**Practice Exercise: Network Diagnostic Script**
```bash
#!/bin/bash
# network-check.sh - Basic network diagnostics

echo "=== Network Diagnostics ==="
echo ""

echo "1. IP Addresses:"
ip -br addr show
echo ""

echo "2. Default Gateway:"
ip route | grep default
echo ""

echo "3. DNS Servers:"
cat /etc/resolv.conf | grep nameserver
echo ""

echo "4. Internet Connectivity:"
ping -c 2 8.8.8.8 > /dev/null 2>&1 && echo "✓ Can reach 8.8.8.8" || echo "✗ Cannot reach 8.8.8.8"
ping -c 2 google.com > /dev/null 2>&1 && echo "✓ DNS working" || echo "✗ DNS not working"
echo ""

echo "5. Open Ports:"
sudo ss -tlnp
```

**Learning Check**
- [ ] Can view network configuration
- [ ] Can test network connectivity
- [ ] Can transfer files securely
- [ ] Can use SSH effectively
- [ ] Understand basic firewall management

---

### Hour 7: Package Management (4:00 PM - 5:00 PM)

**Theory (10 minutes)**
- Package managers (apt, yum, dnf, snap)
- Repositories
- Dependency resolution
- Package sources

**Hands-On Practice (50 minutes)**

1. **APT (Debian/Ubuntu)**
   ```bash
   # Update package list
   sudo apt update
   
   # Upgrade packages
   sudo apt upgrade
   sudo apt full-upgrade
   
   # Install package
   sudo apt install nginx
   sudo apt install nginx mysql-server
   
   # Remove package
   sudo apt remove nginx
   sudo apt purge nginx         # Remove with config files
   sudo apt autoremove          # Remove unused dependencies
   
   # Search packages
   apt search nginx
   apt-cache search web server
   
   # Package info
   apt show nginx
   apt-cache policy nginx
   
   # List installed packages
   apt list --installed
   apt list --installed | grep nginx
   
   # Which package provides a file
   dpkg -S /usr/bin/curl
   apt-file search bin/curl     # Needs apt-file installed
   
   # Download without installing
   apt download nginx
   
   # Clean cache
   sudo apt clean
   sudo apt autoclean
   ```

2. **Managing .deb Files**
   ```bash
   # Install local .deb
   sudo dpkg -i package.deb
   
   # Fix broken dependencies
   sudo apt --fix-broken install
   
   # Remove package
   sudo dpkg -r package
   
   # List installed
   dpkg -l
   dpkg -l | grep nginx
   
   # Package contents
   dpkg -L nginx
   
   # Check if package installed
   dpkg -s nginx
   ```

3. **YUM/DNF (RedHat/CentOS/Fedora)**
   ```bash
   # Update
   sudo yum update           # RHEL/CentOS 7
   sudo dnf update           # RHEL/CentOS 8+, Fedora
   
   # Install
   sudo yum install nginx
   sudo dnf install nginx
   
   # Remove
   sudo yum remove nginx
   sudo dnf remove nginx
   
   # Search
   yum search nginx
   dnf search nginx
   
   # Info
   yum info nginx
   dnf info nginx
   
   # List installed
   yum list installed
   dnf list installed
   
   # Clean cache
   sudo yum clean all
   sudo dnf clean all
   
   # Repository management
   yum repolist
   dnf repolist
   ```

4. **Snap Packages (Universal)**
   ```bash
   # Install snap
   sudo apt install snapd
   
   # Search snap
   snap find package
   
   # Install
   sudo snap install vscode --classic
   sudo snap install spotify
   
   # List installed
   snap list
   
   # Update
   sudo snap refresh
   sudo snap refresh vscode
   
   # Remove
   sudo snap remove vscode
   
   # Info
   snap info vscode
   ```

5. **Repository Management**
   ```bash
   # Add repository (Ubuntu/Debian)
   sudo add-apt-repository ppa:repository/ppa
   sudo add-apt-repository "deb http://example.com/repo stable main"
   sudo apt update
   
   # Remove repository
   sudo add-apt-repository --remove ppa:repository/ppa
   
   # List repositories
   grep -r --include '*.list' '^deb ' /etc/apt/
   
   # GPG keys
   wget -qO - https://example.com/key.gpg | sudo apt-key add -
   ```

6. **Compile from Source** (when needed)
   ```bash
   # Install build tools
   sudo apt install build-essential
   
   # Download source
   wget https://example.com/software-1.0.tar.gz
   tar -xzf software-1.0.tar.gz
   cd software-1.0
   
   # Typical build process
   ./configure
   make
   sudo make install
   
   # Alternative: checkinstall (creates .deb)
   sudo apt install checkinstall
   sudo checkinstall
   ```

**Common Package Collections**
```bash
# Web server
sudo apt install nginx apache2

# Database
sudo apt install mysql-server postgresql

# Development tools
sudo apt install git curl wget vim build-essential

# Python
sudo apt install python3 python3-pip python3-venv

# Node.js
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install nodejs

# Docker
curl -fsSL https://get.docker.com | sh
```

**Learning Check**
- [ ] Can install/remove packages
- [ ] Can search for packages
- [ ] Can manage repositories
- [ ] Can update system packages
- [ ] Know difference between package managers

---

### Hour 8: System Monitoring & Logs (5:00 PM - 6:00 PM)

**Theory (10 minutes)**
- System resources (CPU, RAM, disk, network)
- Log locations and types
- journalctl vs traditional logs
- Monitoring best practices

**Hands-On Practice (50 minutes)**

1. **Disk Usage**
   ```bash
   # Disk space
   df -h              # Human-readable
   df -h /
   df -i              # Inode usage
   
   # Directory size
   du -sh directory/
   du -sh *           # All items in current dir
   du -h --max-depth=1 /var/log
   
   # Find large files
   find / -type f -size +100M 2>/dev/null
   du -ah / 2>/dev/null | sort -rh | head -20
   
   # Disk info
   lsblk
   sudo fdisk -l
   ```

2. **Memory Usage**
   ```bash
   # Free memory
   free -h
   free -m
   
   # Detailed memory info
   cat /proc/meminfo
   
   # Memory by process
   ps aux --sort=-%mem | head
   
   # Check swap
   swapon --show
   cat /proc/swaps
   ```

3. **CPU Info**
   ```bash
   # CPU details
   lscpu
   cat /proc/cpuinfo
   
   # Number of cores
   nproc
   
   # Load average
   uptime
   w
   cat /proc/loadavg
   
   # CPU usage by process
   ps aux --sort=-%cpu | head
   ```

4. **System Information**
   ```bash
   # Kernel version
   uname -a
   uname -r
   
   # OS version
   cat /etc/os-release
   lsb_release -a
   
   # Uptime
   uptime
   
   # Hardware info
   sudo lshw
   sudo lshw -short
   sudo dmidecode
   
   # USB devices
   lsusb
   
   # PCI devices
   lspci
   ```

5. **Log Files**
   ```bash
   # System logs location
   cd /var/log
   
   # Common log files
   /var/log/syslog          # System messages (Debian/Ubuntu)
   /var/log/messages        # System messages (RHEL/CentOS)
   /var/log/auth.log        # Authentication logs
   /var/log/kern.log        # Kernel logs
   /var/log/dmesg           # Boot messages
   /var/log/cron.log        # Cron job logs
   /var/log/nginx/          # Nginx logs
   /var/log/apache2/        # Apache logs
   
   # View logs
   sudo tail -f /var/log/syslog
   sudo less /var/log/auth.log
   ```

6. **Journalctl (systemd)**
   ```bash
   # View all logs
   sudo journalctl
   
   # Follow (real-time)
   sudo journalctl -f
   
   # Since boot
   sudo journalctl -b
   sudo journalctl -b -1      # Previous boot
   
   # Time range
   sudo journalctl --since "2024-02-22 09:00:00"
   sudo journalctl --since "1 hour ago"
   sudo journalctl --since yesterday
   sudo journalctl --since today
   sudo journalctl --until "2024-02-22 17:00:00"
   
   # Specific service
   sudo journalctl -u nginx
   sudo journalctl -u ssh -f
   
   # Priority level
   sudo journalctl -p err       # Errors only
   sudo journalctl -p warning   # Warnings and above
   
   # Output format
   sudo journalctl -o json
   sudo journalctl -o json-pretty
   
   # Disk usage
   sudo journalctl --disk-usage
   
   # Clean old logs
   sudo journalctl --vacuum-time=7d
   sudo journalctl --vacuum-size=1G
   ```

7. **Monitoring Tools**
   ```bash
   # Real-time monitoring
   top
   htop           # Better alternative
   glances        # All-in-one monitoring
   
   # I/O monitoring
   iotop          # Disk I/O by process
   iostat         # I/O statistics
   
   # Network monitoring
   iftop          # Network traffic by connection
   nethogs        # Network traffic by process
   vnstat         # Network statistics
   
   # Install tools
   sudo apt install htop glances iotop sysstat iftop nethogs vnstat
   ```

**Practice Exercise: System Health Check Script**
```bash
#!/bin/bash
# health-check.sh - System health monitoring

echo "=== SYSTEM HEALTH CHECK ==="
echo "Date: $(date)"
echo ""

# Uptime
echo "Uptime:"
uptime
echo ""

# Disk Usage
echo "Disk Usage:"
df -h | grep -vE '^Filesystem|tmpfs|cdrom'
echo ""

# Memory Usage
echo "Memory Usage:"
free -h
echo ""

# CPU Load
echo "CPU Load (1/5/15 min):"
cat /proc/loadavg | awk '{print $1, $2, $3}'
echo ""

# Top 5 CPU processes
echo "Top 5 CPU Processes:"
ps aux --sort=-%cpu | head -6 | tail -5
echo ""

# Top 5 Memory processes
echo "Top 5 Memory Processes:"
ps aux --sort=-%mem | head -6 | tail -5
echo ""

# Failed services
echo "Failed Services:"
systemctl --failed
echo ""

# Recent errors
echo "Recent Errors (last 10):"
sudo journalctl -p err -n 10 --no-pager
```

**Learning Check**
- [ ] Can monitor disk usage
- [ ] Can check memory and CPU
- [ ] Can view and analyze logs
- [ ] Can use journalctl effectively
- [ ] Can create monitoring scripts

---

## 🎯 Day 0 Completion Checklist

### Knowledge Verification
- [ ] Understand Linux file system hierarchy
- [ ] Can navigate file system without GUI
- [ ] Master file permissions (rwx, chmod, chown)
- [ ] Can use grep, sed, awk for text processing
- [ ] Understand process management and signals
- [ ] Can manage users and groups
- [ ] Comfortable with networking commands
- [ ] Can install/remove packages
- [ ] Know how to monitor system resources
- [ ] Can analyze log files

### Practical Skills
- [ ] Created and ran shell scripts
- [ ] Set up proper file permissions
- [ ] Killed and managed processes
- [ ] Configured users and groups
- [ ] Transferred files via SCP/rsync
- [ ] Configured SSH keys
- [ ] Managed system services
- [ ] Monitored system health
- [ ] Analyzed logs with journalctl
- [ ] Built automation scripts

### Projects Completed
- [ ] Server Setup Automation Script
- [ ] User Management System
- [ ] Log Analysis Tool
- [ ] System Health Monitor

---

## 📚 Additional Resources

**Cheat Sheets**
- [Linux Command Cheat Sheet](https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/)
- [Bash Scripting Cheat Sheet](https://devhints.io/bash)

**Interactive Practice**
- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) - Security challenges
- [Linux Journey](https://linuxjourney.com/) - Interactive tutorials
- [Exercism Linux Track](https://exercism.org/tracks/bash)

**Videos**
- [Linux Crash Course](https://www.youtube.com/watch?v=ROjZy1WbCIA)
- [Bash Scripting Full Course](https://www.youtube.com/watch?v=tK9Oc6AEnR4)

---

## 🎓 What's Next?

After mastering Day 0, you're ready for:
- **Day 2**: Docker Basics (containerization)
- **Day 3**: Docker Compose (multi-container apps)
- **Day 4**: Git & GitHub (version control)
- **Day 5-8**: Kubernetes Journey

**Remember:** Linux is the foundation of EVERYTHING in DevOps. The time you invest today will pay dividends throughout your entire journey!

---

**Congratulations on completing Day 0! You're now ready to tackle the DevOps world! 🚀**
