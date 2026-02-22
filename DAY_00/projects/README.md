# Day 0: Linux Fundamentals - Hands-On Projects

## 🎯 Overview

These 4 projects will solidify your Linux skills by building **real DevOps tools** that you'll actually use in production environments. Each project progressively builds on the skills learned throughout the day.

**Time Investment:** 2-3 hours total (30-45 min per project)  
**Difficulty:** Beginner to Intermediate  
**Skills Applied:** All 8 hours of learning combined

---

## 📊 Projects at a Glance

| Project | Skills | Time | Complexity | DevOps Relevance |
|---------|--------|------|------------|------------------|
| [1. Server Setup Automation](#project-1-server-setup-automation) | File ops, Packages, Permissions | 30 min | ⭐⭐ | High - IaC foundation |
| [2. Multi-User Environment](#project-2-multi-user-environment-manager) | Users, Groups, Permissions, Security | 45 min | ⭐⭐⭐ | Medium - Team management |
| [3. Log Analyzer](#project-3-log-analyzer-tool) | Text processing, Grep, Awk, Pipes | 45 min | ⭐⭐⭐ | Very High - Debugging |
| [4. System Monitor](#project-4-system-health-monitor) | Processes, Resources, Systemd, Logs | 60 min | ⭐⭐⭐⭐ | Very High - Production ops |

---

## 🏗️ Project 1: Server Setup Automation

**What You'll Build:** A bash script that automates initial server configuration - the first thing you'd do when spinning up a new VM.

### Objectives
- Update system packages
- Install essential tools
- Configure firewall
- Set up SSH hardening
- Create deployment directory structure
- Generate setup report

### Skills Applied
- File operations
- Package management
- Permissions
- Basic security

### Step-by-Step Guide

**Full detailed guide:** [projects/server-setup/README.md](server-setup/README.md)

**Quick Overview:**
```bash
cd ~/Devops_Roadmap/DAY_00/projects/server-setup

# Your script will:
# 1. Update and upgrade packages
# 2. Install: git, curl, vim, htop, docker, nginx
# 3. Configure UFW (allow SSH, HTTP, HTTPS)
# 4. Create /var/www/apps directory structure
# 5. Set proper permissions
# 6. Generate log file with all actions
```

### Success Criteria
- [ ] Script runs without errors on fresh Ubuntu/Debian system
- [ ] All packages installed successfully
- [ ] Firewall configured correctly
- [ ] Directory structure created with proper permissions
- [ ] Log file contains all actions with timestamps

### DevOps Connection
🔗 **Where you'll use this:**
- **IaC (Day 22-23):** This is manual version of Ansible/Terraform
- **CI/CD (Day 15-17):** Jenkins agents need similar setup
- **Cloud (Day 18-21):** AWS EC2/Azure VMs require post-launch config

---

## 👥 Project 2: Multi-User Environment Manager

**What You'll Build:** A tool to set up collaborative development environments with proper user isolation and group permissions.

### Objectives
- Create multiple users with different roles
- Set up shared project directories
- Configure group-based permissions
- Implement sudo policies
- Generate user credentials report

### Skills Applied
- User and group management
- Advanced permissions (SGID, sticky bit)
- Sudo configuration
- Security best practices

### Step-by-Step Guide

**Full detailed guide:** [projects/user-management/README.md](user-management/README.md)

**Quick Overview:**
```bash
cd ~/Devops_Roadmap/DAY_00/projects/user-management

# Your script will create:
# - 3 developers (dev1, dev2, dev3)
# - 2 devops engineers (ops1, ops2)
# - 1 manager (manager1)

# With:
# - Shared project directory: /projects/webapp
# - Developers can read/write in group area
# - DevOps can sudo specific commands
# - Manager can read all logs
```

### Success Criteria
- [ ] All users created with proper home directories
- [ ] Group permissions allow collaboration
- [ ] Sticky bit prevents accidental deletion
- [ ] Sudo configured for DevOps team only
- [ ] Password policies enforced

### DevOps Connection
🔗 **Where you'll use this:**
- **Kubernetes (Days 3-8):** RBAC is user management at scale
- **CI/CD (Day 15-17):** Build users need specific permissions
- **Security (Day 14):** Principle of least privilege

---

## 🔍 Project 3: Log Analyzer Tool

**What You'll Build:** A bash script that parses, filters, and analyzes log files - the most critical debugging skill in DevOps.

### Objectives
- Parse multiple log formats (syslog, Apache, Nginx)
- Extract error patterns
- Generate statistics
- Create summary reports
- Alert on critical issues

### Skills Applied
- Grep with regex
- Awk for field extraction
- Sed for text transformation
- Pipes for complex processing
- Array manipulation in bash

### Step-by-Step Guide

**Full detailed guide:** [projects/log-analyzer/README.md](log-analyzer/README.md)

**Quick Overview:**
```bash
cd ~/Devops_Roadmap/DAY_00/projects/log-analyzer

# Your script will:
# 1. Accept log file as input
# 2. Count total lines, errors, warnings
# 3. Extract top 10 error patterns
# 4. Find top IP addresses (if web log)
# 5. Generate time-based analysis
# 6. Output HTML report
```

**Sample Output:**
```
=== Log Analysis Report ===
File: /var/log/syslog
Period: 2024-02-22 09:00 to 2024-02-22 17:00

Total Lines: 15,432
Errors: 23
Warnings: 145
Info: 15,264

Top 5 Error Patterns:
  12 - "Failed to connect to database"
   5 - "Permission denied"
   3 - "Out of memory"
   2 - "Connection timeout"
   1 - "Disk full"

Time Distribution:
  09:00-12:00: 3,245 lines (4 errors)
  12:00-15:00: 6,821 lines (12 errors)
  15:00-17:00: 5,366 lines (7 errors)
```

### Success Criteria
- [ ] Correctly parses syslog format
- [ ] Extracts and counts error types
- [ ] Generates time-based statistics
- [ ] Outputs both terminal and HTML reports
- [ ] Handles large files (100MB+) efficiently

### DevOps Connection
🔗 **Where you'll use this:**
- **Every Single Day:** Debugging production issues
- **Monitoring (Day 26-27):** Basis for alert rules
- **Kubernetes (Days 3-8):** Pod logs are critical
- **CI/CD (Day 15-17):** Build failure analysis

---

## 📊 Project 4: System Health Monitor

**What You'll Build:** A comprehensive monitoring script that tracks system resources, services, and generates alerts - a mini version of Prometheus/Grafana.

### Objectives
- Monitor CPU, memory, disk, network
- Check critical service status
- Track process resource usage
- Generate health score
- Send alerts when thresholds exceeded
- Create historical trend data

### Skills Applied
- Process management
- System monitoring commands
- Journalctl for service logs
- Cron for scheduling
- File I/O for data storage
- Conditional logic for alerting

### Step-by-Step Guide

**Full detailed guide:** [projects/system-monitor/README.md](system-monitor/README.md)

**Quick Overview:**
```bash
cd ~/Devops_Roadmap/DAY_00/projects/system-monitor

# Your script will monitor:
# - CPU usage (alert if > 80%)
# - Memory usage (alert if > 85%)
# - Disk space (alert if > 90%)
# - Critical services (nginx, docker, ssh)
# - Top resource-consuming processes
# - Network connectivity

# Output:
# - Real-time dashboard (terminal)
# - JSON metrics file
# - Alert log
# - Historical trends (CSV)
```

**Sample Dashboard:**
```
╔══════════════════════════════════════════════════════╗
║        SYSTEM HEALTH MONITOR - Feb 22, 17:30        ║
╠══════════════════════════════════════════════════════╣
║ Overall Health: ████████░░ 82% (GOOD)               ║
╠══════════════════════════════════════════════════════╣
║ CPU Usage:      ████░░░░░░ 38% ✓                    ║
║ Memory:         ██████░░░░ 62% ✓                    ║
║ Disk /:         ███████░░░ 73% ✓                    ║
║ Load Average:   1.23, 1.45, 1.67                    ║
╠══════════════════════════════════════════════════════╣
║ Services:                                            ║
║  ✓ nginx         Running  (PID: 1234)               ║
║  ✓ docker        Running  (PID: 5678)               ║
║  ✗ mysql         Stopped  [ALERT]                   ║
║  ✓ ssh           Running  (PID: 910)                ║
╠══════════════════════════════════════════════════════╣
║ Top Processes:                                       ║
║  1. chrome       2.3 GB  (45% CPU)                  ║
║  2. node         1.1 GB  (12% CPU)                  ║
║  3. docker       856 MB  (8% CPU)                   ║
╠══════════════════════════════════════════════════════╣
║ Alerts: 1 new                                        ║
║  🚨 MySQL service is down!                          ║
╚══════════════════════════════════════════════════════╝
```

### Success Criteria
- [ ] Monitors all key resources accurately
- [ ] Checks service status via systemctl
- [ ] Generates ASCII dashboard
- [ ] Creates JSON metrics for parsing
- [ ] Logs alerts to separate file
- [ ] Can run as cron job (every 5 minutes)
- [ ] Handles edge cases (services not installed, etc.)

### DevOps Connection
🔗 **Where you'll use this:**
- **Production Operations:** Daily health checks
- **Monitoring (Day 26-27):** Prometheus/Grafana do this at scale
- **Kubernetes (Days 3-8):** kubectl top nodes/pods
- **CI/CD (Day 15-17):** Jenkins agent health
- **Cloud (Day 18-21):** CloudWatch/Azure Monitor alternative

---

## 🚀 Getting Started

### Prerequisites
```bash
# Ensure you have:
- Linux system (Ubuntu 20.04+ recommended)
- Sudo access
- 2-3 hours of focused time
- Completed DAY_0_PLAN.md (or at least hours 1-8)
```

### Setup
```bash
# Navigate to projects directory
cd ~/Devops_Roadmap/DAY_00/projects

# Each project has its own folder:
ls -la

# Output:
# drwxr-xr-x server-setup/
# drwxr-xr-x user-management/
# drwxr-xr-x log-analyzer/
# drwxr-xr-x system-monitor/
```

### Recommended Order
1. **Start with Project 1** (Server Setup) - Easiest, builds confidence
2. **Then Project 2** (User Management) - Introduces security concepts
3. **Next Project 3** (Log Analyzer) - Most practical skill
4. **Finish with Project 4** (System Monitor) - Ties everything together

---

## 📝 Project Submission Checklist

For each project, ensure you have:

- [ ] Working script with proper shebang (`#!/bin/bash`)
- [ ] Executable permissions (`chmod +x script.sh`)
- [ ] Comments explaining each section
- [ ] Error handling (check command exit codes)
- [ ] Usage instructions in README.md
- [ ] Sample output/screenshots
- [ ] Git commit with descriptive message

**Example Commit:**
```bash
git add DAY_00/projects/server-setup/
git commit -m "Complete Project 1: Server Setup Automation

- Automated package installation (git, docker, nginx)
- Configured UFW firewall rules
- Created deployment directory structure
- Added comprehensive logging
- Tested on Ubuntu 22.04"
```

---

## 🎓 Learning Outcomes

After completing all 4 projects, you will have:

### Technical Skills
- ✅ Written production-ready bash scripts
- ✅ Automated server configuration
- ✅ Managed users and permissions at scale
- ✅ Parsed and analyzed complex log files
- ✅ Built system monitoring tools
- ✅ Implemented error handling and logging
- ✅ Created user-friendly output (dashboards, reports)

### DevOps Skills
- ✅ Infrastructure as Code mindset
- ✅ Security best practices
- ✅ Debugging and troubleshooting
- ✅ Monitoring and alerting
- ✅ Automation thinking
- ✅ Production readiness

### Portfolio Pieces
- ✅ 4 GitHub-ready projects
- ✅ Demonstrate Linux mastery
- ✅ Show problem-solving ability
- ✅ Prove automation skills

---

## 🔗 Integration with Learning Path

### How Projects Map to DevOps Roadmap

| Project | Day 2-8 (Docker/K8s) | Day 15-17 (CI/CD) | Day 18-21 (Cloud) | Day 22-25 (IaC) |
|---------|----------------------|-------------------|-------------------|-----------------|
| Server Setup | Container host config | Jenkins agent setup | EC2 post-launch | Ansible playbook basis |
| User Mgmt | Container users | Git access control | IAM roles concept | Permission automation |
| Log Analyzer | Container logs | Build logs parsing | CloudWatch query | Log aggregation |
| System Monitor | Resource limits | Build metrics | CloudWatch alternative | Monitoring as code |

---

## 📚 Additional Challenges (Optional)

If you finish all 4 projects and want more:

### Challenge 1: Combine All Projects
Create a **master DevOps toolkit** script that:
- Sets up server (Project 1)
- Creates users (Project 2)
- Installs log analyzer (Project 3)
- Schedules system monitor (Project 4)

### Challenge 2: Add Advanced Features
- **Project 1:** Add Docker Compose installation
- **Project 2:** Implement password rotation
- **Project 3:** Add email alerts for critical errors
- **Project 4:** Generate Grafana-compatible metrics

### Challenge 3: Containerize
- Package each project in a Docker container
- Create Docker Compose setup
- Test in Kubernetes (preview for Days 3-8!)

---

## 🆘 Troubleshooting

### Common Issues

**Issue:** Script fails with "Permission denied"
```bash
# Solution: Make script executable
chmod +x script.sh
```

**Issue:** Sudo commands fail
```bash
# Solution: Run with sudo or add to sudoers
sudo ./script.sh
```

**Issue:** Package installation fails
```bash
# Solution: Update package list first
sudo apt update
```

**Issue:** Can't access log files
```bash
# Solution: Logs require sudo
sudo cat /var/log/syslog
```

---

## 🎯 Success Metrics

You'll know you've mastered this when:

- [ ] All 4 projects run successfully
- [ ] Scripts handle errors gracefully
- [ ] Code is well-commented and readable
- [ ] You can explain every command used
- [ ] Projects are committed to Git
- [ ] You're excited to show someone your work!

---

## 📖 Resources

### Documentation
- [Bash Scripting Guide](https://www.gnu.org/software/bash/manual/)
- [Linux Command Reference](https://linux.die.net/)
- [Systemd Documentation](https://systemd.io/)

### Tools
- [ShellCheck](https://www.shellcheck.net/) - Lint your bash scripts
- [Explain Shell](https://explainshell.com/) - Understand complex commands
- [Bash One-Liners](https://github.com/onceupon/Bash-Oneliner) - Quick references

### Testing
```bash
# Test your scripts in Docker:
docker run -it ubuntu:22.04 /bin/bash

# Then run your script inside container
```

---

## 🎉 Celebration Time!

When you complete all 4 projects:

1. **Document Your Work:** Take screenshots, write a blog post
2. **Update Resume:** Add "Linux System Administration" skill
3. **LinkedIn Post:** Share your learning journey
4. **GitHub:** Push all projects, add README badges
5. **Treat Yourself:** You've earned it! 🍕

---

## ➡️ Next Steps

**After Projects:**
1. Review day-00-notes.md
2. Update progress in DAY_00/README.md
3. Commit everything to Git
4. Move to **DAY_01: DevOps Roadmap Setup**

**Keep Practicing:**
- Run system monitor daily
- Analyze real logs weekly
- Automate repetitive tasks
- Contribute to open-source projects

---

**Ready to build? Pick your first project and dive in!**

**[Start with Project 1: Server Setup →](server-setup/README.md)**

---

**Remember:** Every DevOps engineer started exactly where you are now. The only difference between you and them is time and practice. You've got this! 💪
