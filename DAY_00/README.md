# Day 0: Linux Fundamentals - The DevOps Foundation

## 🎯 Overview

**Welcome to Day 0** - The foundation of ALL DevOps skills! Before diving into Docker, Kubernetes, and cloud platforms, you MUST master Linux. This is non-negotiable for any DevOps engineer.

> 💡 **Why Linux First?** 95% of servers run Linux. Docker containers run Linux. Kubernetes orchestrates Linux containers. AWS/Azure VMs run Linux. Master this, master DevOps.

## ⏰ Time Commitment

**8 hours** of intensive hands-on Linux practice

## 🎓 What You'll Master Today

### Core Linux Skills
- **File System & Navigation** - Move like a pro through directories
- **File Permissions** - chmod, chown, umask mastery
- **Process Management** - ps, top, kill, systemctl
- **User & Group Management** - useradd, usermod, sudo
- **Package Management** - apt, yum, dnf, snap
- **Networking Basics** - ifconfig, ip, netstat, ss
- **Text Processing** - grep, sed, awk, cut, sort
- **Shell Scripting** - Bash automation fundamentals
- **System Monitoring** - df, du, free, htop
- **Log Management** - journalctl, /var/log exploration

### Hands-On Projects
1. **Server Setup Script** - Automate server configuration
2. **User Management System** - Multi-user environment setup
3. **Log Analysis Tool** - Parse and analyze system logs
4. **System Monitor** - Resource usage tracking script

## 📋 Prerequisites

- macOS/Linux computer (or WSL2 on Windows)
- Terminal access
- Eager to learn mindset!
- No prior Linux experience needed

## 🗂️ Folder Structure

```
DAY_00/
├── README.md                 # This file
├── docs/
│   ├── DAY_0_PLAN.md        # Complete 8-hour schedule
│   └── DAY_0_START.md       # Quick 30-min start guide
├── notes/
│   └── day-00-notes.md      # Your learning journal
└── projects/
    ├── README.md            # All 4 projects
    ├── server-setup/        # Project 1: Automation
    ├── user-management/     # Project 2: Multi-user
    ├── log-analyzer/        # Project 3: Log parsing
    └── system-monitor/      # Project 4: Monitoring
```

## 🚀 Quick Start

Want to jump in immediately? Start with [DAY_0_START.md](docs/DAY_0_START.md) for a 30-minute crash course!

For the complete 8-hour deep dive, see [DAY_0_PLAN.md](docs/DAY_0_PLAN.md).

## 🎯 Learning Objectives

By the end of Day 0, you will:
- ✅ Navigate the Linux file system confidently
- ✅ Manage files and directories with ease
- ✅ Understand and set proper permissions
- ✅ Monitor and manage processes
- ✅ Create and manage users/groups
- ✅ Install and update software packages
- ✅ Analyze system logs effectively
- ✅ Write basic shell scripts
- ✅ Troubleshoot common Linux issues
- ✅ Use SSH securely

## 💻 Essential Commands You'll Master

```bash
# File & Directory Operations (Hour 1)
ls, cd, pwd, mkdir, rmdir, touch, cp, mv, rm, find, locate

# File Permissions (Hour 2)
chmod, chown, chgrp, umask, ls -l, stat

# Text Processing (Hour 3)
cat, less, more, head, tail, grep, sed, awk, cut, sort, uniq, wc

# Process Management (Hour 4)
ps, top, htop, kill, killall, pkill, bg, fg, jobs, systemctl

# User Management (Hour 5)
useradd, usermod, userdel, passwd, su, sudo, groups, id

# Networking (Hour 6)
ip, ifconfig, netstat, ss, ping, traceroute, curl, wget, ssh, scp

# Package Management (Hour 7)
apt/apt-get, yum, dnf, snap, dpkg, rpm

# System Info & Monitoring (Hour 8)
df, du, free, uptime, uname, lsblk, dmesg, journalctl
```

## 📊 Why This Matters for DevOps

| Linux Skill | DevOps Application |
|-------------|-------------------|
| **File Permissions** | Container security, Kubernetes secrets |
| **Process Management** | Docker container troubleshooting |
| **Networking** | Service mesh, load balancing, firewalls |
| **Shell Scripting** | CI/CD automation, deployment scripts |
| **Log Analysis** | Debugging production issues |
| **Package Management** | Infrastructure provisioning |
| **User Management** | IAM policies, access control |
| **System Monitoring** | Observability, alerting |

## 🎓 Skills You'll Gain

After completing Day 0:
- **Command Line Mastery** - Terminal is your primary interface
- **System Administration** - Manage Linux servers confidently
- **Automation Skills** - Write bash scripts for repetitive tasks
- **Troubleshooting** - Debug and fix Linux issues
- **Security Awareness** - Proper permissions and access control
- **DevOps Foundation** - Ready for Docker, K8s, and cloud

## 📈 Progress Tracking

Track your progress as you go:

- [ ] Completed Hour 1: File System Navigation
- [ ] Completed Hour 2: File Permissions & Ownership
- [ ] Completed Hour 3: Text Processing & Filters
- [ ] Completed Hour 4: Process Management
- [ ] Completed Hour 5: User & Group Management
- [ ] Completed Hour 6: Networking Basics
- [ ] Completed Hour 7: Package Management
- [ ] Completed Hour 8: System Monitoring & Logs
- [ ] Completed Project 1: Server Setup Script
- [ ] Completed Project 2: User Management System
- [ ] Completed Project 3: Log Analysis Tool
- [ ] Completed Project 4: System Monitor
- [ ] Documented learning in notes

## 🔗 Resources

**Official Documentation**
- [Linux Command Line Basics](https://ubuntu.com/tutorials/command-line-for-beginners)
- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/)
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/)

**Video Tutorials**
- [Linux Full Course - freeCodeCamp (7hrs)](https://www.youtube.com/watch?v=wBp0Rb-ZJak)
- [Linux for Beginners - NetworkChuck](https://www.youtube.com/watch?v=gd7BXuUQ91w)

**Interactive Learning**
- [Linux Survival](https://linuxsurvival.com/)
- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/)
- [Linux Journey](https://linuxjourney.com/)

**Books**
- "The Linux Command Line" by William Shotts
- "How Linux Works" by Brian Ward

## ⏭️ What's Next?

**After Day 0, you'll be ready for:**
- Day 1: Planning & Setup (Already done!)
- Day 2: Docker Basics
- Day 3: Docker Compose
- Day 4-8: Kubernetes Journey

## 💡 Pro Tips

1. **Practice in a Safe Environment** - Use a VM or container
2. **Read Man Pages** - `man command` is your best friend
3. **Use Tab Completion** - Press Tab to auto-complete
4. **History is Powerful** - Use `history` and `Ctrl+R`
5. **Aliases Save Time** - Create shortcuts in `~/.bashrc`
6. **Google is OK** - But understand what you copy
7. **Break Things** - Best way to learn (in a safe env)
8. **Document Everything** - Take notes in day-00-notes.md

## 🚨 Important Notes

- **macOS Users**: Most commands work the same, but some differ (especially package management)
- **Windows Users**: Use WSL2 (Windows Subsystem for Linux) for best experience
- **VM Option**: Install Ubuntu VM using VirtualBox/VMware
- **Cloud Option**: Use free tier AWS EC2 or Azure VM for practice

## 📞 Need Help?

- Check the [Linux subreddit](https://reddit.com/r/linux4noobs)
- Join [Linux Discord communities](https://discord.gg/linux)
- Stack Overflow for specific questions
- Man pages: `man <command>` or `<command> --help`

---

## 🎯 Today's Success Criteria

You've mastered Day 0 when you can:
- ✅ Navigate entire file system without GUI
- ✅ Set proper file permissions confidently
- ✅ Kill unresponsive processes
- ✅ Create users and manage groups
- ✅ Install/remove packages
- ✅ Parse log files for errors
- ✅ Write a basic bash script
- ✅ Monitor system resources
- ✅ Troubleshoot common issues

---

**Ready to become a Linux power user? Let's get started! 🚀**

Start with [DAY_0_PLAN.md](docs/DAY_0_PLAN.md) for the full 8-hour journey, or [DAY_0_START.md](docs/DAY_0_START.md) for a quick 30-minute introduction!
