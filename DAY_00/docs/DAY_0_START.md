# Day 0: Linux Fundamentals - 30-Minute Quick Start

## 🚀 Get Started in 30 Minutes!

Don't have 8 hours right now? No problem! This quick start guide will teach you the **20% of Linux commands you'll use 80% of the time**.

## ⏰ Time Breakdown

- **10 minutes**: Essential file operations
- **10 minutes**: Text processing and searching
- **10 minutes**: Process and system monitoring

---

## 📁 Part 1: Essential File Operations (10 min)

### Navigate Like a Pro
```bash
# Where am I?
pwd

# What's here?
ls
ls -la          # Detailed list with hidden files

# Go places
cd /var/log     # Absolute path
cd ..           # Parent directory
cd ~            # Home directory
cd -            # Previous directory
```

### File Manipulation
```bash
# Create
touch file.txt
mkdir mydir

# Copy
cp file.txt backup.txt
cp -r mydir mydir_backup

# Move/Rename
mv file.txt newname.txt

# Delete
rm file.txt
rm -rf mydir    # CAREFUL! No undo!

# View files
cat file.txt         # Show all
less file.txt        # Page through (q to quit)
head -10 file.txt    # First 10 lines
tail -20 file.txt    # Last 20 lines
tail -f /var/log/syslog  # Follow in real-time
```

### **Quick Win #1: Find Files Fast**
```bash
# Find by name
find /home -name "*.txt"
find . -type f -name "config"

# Find by size
find /var/log -size +100M

# Search text in files
grep -r "ERROR" /var/log/
```

**Try it now:**
```bash
# Create test files
mkdir ~/linux-practice
cd ~/linux-practice
touch file1.txt file2.log file3.txt

# Find all .txt files
find . -name "*.txt"

# Create a file with content
echo "Hello Linux!" > greeting.txt
cat greeting.txt
```

---

## 🔐 Part 2: Permissions (5 min)

### Understanding Permissions
```
-rw-r--r--  1 user group 1234 Feb 22 09:00 file.txt
 │││ │││ │││
 │││ │││ └── Others can read
 │││ └────── Group can read
 └────────── Owner can read and write
```

### Change Permissions
```bash
# Make script executable
chmod +x script.sh

# Common patterns
chmod 755 file    # rwxr-xr-x (scripts, programs)
chmod 644 file    # rw-r--r-- (regular files)
chmod 700 file    # rwx------ (private files)

# Change owner
sudo chown user:group file.txt
```

**Quick Win #2: Make Your First Script**
```bash
# Create script
cat > hello.sh << 'EOF'
#!/bin/bash
echo "Hello, $(whoami)!"
echo "You are in: $(pwd)"
EOF

# Make executable
chmod +x hello.sh

# Run it
./hello.sh
```

---

## 🔍 Part 3: Text Processing (10 min)

### Grep - Search Text
```bash
# Find in file
grep "pattern" file.txt

# Case-insensitive
grep -i "error" log.txt

# Recursive search
grep -r "TODO" /path/to/project

# With line numbers
grep -n "function" script.py

# Count matches
grep -c "ERROR" log.txt
```

### Pipes - Chain Commands
```bash
# Combine commands
cat file.txt | grep "error" | wc -l

# Sort and unique
cat names.txt | sort | uniq

# Process log files
cat access.log | grep "404" | awk '{print $1}' | sort | uniq -c
```

**Quick Win #3: Analyze Logs**
```bash
# Create sample log
cat > access.log << 'EOF'
192.168.1.1 - GET /index.html 200
192.168.1.2 - GET /about.html 404
192.168.1.1 - POST /api/data 200
192.168.1.3 - GET /contact.html 404
EOF

# Count 404 errors
grep "404" access.log | wc -l

# Find unique IP addresses
awk '{print $1}' access.log | sort | uniq
```

---

## ⚙️ Part 4: Process Management (5 min)

### View Processes
```bash
# All processes
ps aux

# Find specific process
ps aux | grep nginx

# Real-time monitoring
top         # Press 'q' to quit
htop        # Better alternative (if installed)
```

### Kill Processes
```bash
# Find process ID
ps aux | grep process_name

# Kill gracefully
kill PID

# Force kill
kill -9 PID

# Kill by name
pkill process_name
```

**Quick Win #4: Monitor System**
```bash
# Quick system check
uptime                    # How long system is running
free -h                   # Memory usage
df -h                     # Disk space
ps aux --sort=-%cpu | head -5  # Top CPU users
```

---

## 🌐 Part 5: Essential Networking (5 min)

### Network Commands
```bash
# Check connectivity
ping google.com
ping -c 4 8.8.8.8    # 4 packets only

# Download files
wget https://example.com/file.txt
curl -O https://example.com/file.txt

# Check open ports
sudo netstat -tulpn
sudo ss -tulpn       # Modern alternative

# Connect to remote server
ssh user@hostname
scp file.txt user@hostname:/path/
```

---

## 📦 Part 6: Package Management (5 min)

### Ubuntu/Debian (apt)
```bash
# Update package list
sudo apt update

# Install package
sudo apt install nginx

# Remove package
sudo apt remove nginx

# Search packages
apt search nginx
```

### Quick Package Install
```bash
# Essential tools
sudo apt install -y \
    curl \
    wget \
    git \
    vim \
    htop \
    net-tools
```

---

## 🎓 30-Minute Challenge: Complete This Exercise!

Put everything together in one real-world scenario:

```bash
# 1. Set up workspace
mkdir ~/devops-test
cd ~/devops-test

# 2. Create a monitoring script
cat > monitor.sh << 'EOF'
#!/bin/bash
echo "=== Quick System Check ==="
echo "Date: $(date)"
echo "Uptime: $(uptime | awk -F'up ' '{print $2}' | awk -F',' '{print $1}')"
echo "Disk: $(df -h / | tail -1 | awk '{print $5 " used"}')"
echo "Memory: $(free -h | grep Mem | awk '{print $3 "/" $2}')"
echo "Top process: $(ps aux --sort=-%cpu | head -2 | tail -1 | awk '{print $11}')"
EOF

# 3. Make it executable
chmod +x monitor.sh

# 4. Run it
./monitor.sh

# 5. Create a cron job to run every hour (optional)
# echo "0 * * * * /home/$(whoami)/devops-test/monitor.sh >> /tmp/monitor.log" | crontab -
```

---

## ✅ Quick Reference Card

**Save this for daily use:**

```bash
# Navigation
pwd, ls, cd, mkdir, touch

# File Operations
cp, mv, rm, cat, less, head, tail

# Search
find, grep, locate

# Permissions
chmod, chown, ls -l

# Processes
ps, top, kill, killall

# Networking
ping, curl, wget, ssh, scp

# Package Management
sudo apt update
sudo apt install package

# System Info
uptime, free -h, df -h, uname -a

# Help
man command
command --help
```

---

## 🚀 What's Next?

### Immediate (Right Now)
1. Practice these commands in your terminal
2. Complete the 30-minute challenge above
3. Create your own test scripts

### Today (If You Have Time)
- Go through the full [DAY_0_PLAN.md](DAY_0_PLAN.md) (8 hours)
- Complete all 4 hands-on projects
- Take detailed notes

### This Week
- Practice daily (even 15 minutes helps!)
- Explore man pages: `man ls`, `man grep`, etc.
- Try [OverTheWire Bandit](https://overthewire.org/wargames/bandit/)

---

## 💡 Pro Tips for Beginners

1. **Tab Completion is Your Friend**
   - Type first few letters and press Tab
   - Double Tab to see all options

2. **Use History**
   - Up/Down arrows for previous commands
   - `Ctrl+R` to search command history
   - `history` to see all commands

3. **Man Pages Are Documentation**
   - `man command` shows manual
   - `/pattern` to search in man page
   - `q` to quit

4. **Don't Fear Breaking Things**
   - Practice in a VM or container
   - Linux is forgiving (except `rm -rf /`)
   - You learn most from mistakes!

5. **Google is OK**
   - Everyone searches for commands
   - But try to understand before copy-paste
   - Ask "why" not just "how"

---

## 🎯 Success Metrics

After this 30-minute session, you should be able to:
- ✅ Navigate the file system confidently
- ✅ Create, modify, and delete files
- ✅ Search for files and text
- ✅ Change file permissions
- ✅ Monitor system resources
- ✅ Run basic networking commands
- ✅ Install packages

---

## 📚 Want to Go Deeper?

1. **Full Day Plan**: [DAY_0_PLAN.md](DAY_0_PLAN.md) - Complete 8-hour deep dive
2. **Projects**: [projects/README.md](../projects/README.md) - 4 hands-on projects
3. **Notes**: [day-00-notes.md](../notes/day-00-notes.md) - Document your learning

---

**Congratulations! You've just learned the core Linux skills that will serve you throughout your entire DevOps career! 🎉**

**Ready for more? Move on to the [full 8-hour plan](DAY_0_PLAN.md) or start building the [hands-on projects](../projects/README.md)!**
