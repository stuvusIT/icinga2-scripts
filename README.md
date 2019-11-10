# icinga2-scripts

This role installs commonly used scripts for Icinga 2.

Currently, the following scripts are installed:

- `check_dns_recursion` - Checks whether random domain names are successfully recursed.
- `check_dns_repl` - Checks whether DNS zones are successfully replicated.
- `check_dnssec` - Checks whether a zone returns valid authenticated data.
- `check_dsync` - Checks whether dovecot mailboxes failed to replicate.
- `check_free` - Checks if the machine has enough available memory.
- `check_hddtemp` - Checks the temperature of all attached SCSI-like devices.
- `check_jenkins` - Checks a Jenkins instance via the [Metrics plugin](https://wiki.jenkins.io/display/JENKINS/Metrics+Plugin).
- `check_kernel` - Checks if the machine needs to be rebooted in order to apply a kernel update.
- `check_rdp` - Checks if an RDP connection works.
- `check_redis` - Checks if a connection to a Redis server can be established.
- `check_services` - Checks if any systemd services failed (systemctl --failed).
- `check_tty` - Checks if a TTY is idling for a long time.
- `check_unifi` - Checks if all APs in a Unifi controller are reachable and up to date.
- `check_zfs` - Checks the health, free space and fragmentation of a ZFS pool.
- `check_zfs_snapshot` - Checks the age of the most-recent snapshot of ZFS datasets.
- `check_zpool_scrub` - Checks if a scrub has been performed recently on ZFS pools.
- `notify_host_mattermost` - Notifies a host state in a Mattermost channel.
- `notify_host_msmtp` - Notifies a host state via msmtp mail.
- `notify_service_mattermost` - Notifies a service state in a Mattermost channel.
- `notify_service_msmtp` - Notifies a service state via msmtp mail.

## Requirements

Debian

## Role Variables

| Name                                 | Default/Required         | Description                                         |
|--------------------------------------|:------------------------:|-----------------------------------------------------|
| `icinga2_scripts_path`               | `/usr/lib/stuvus/icinga` | Path where the scripts are installed to             |
| `icinga2_needs_notification_scripts` | `false`                  | Whether to install the notification scripts as well |
| `icinga2_needs_tinkerforge`          | `false`                  | Whether to install the tinkerforge api as well      |

## Example Playbook

```yml
- hosts: all
  roles:
  - icinga2-scripts

- hosts: icinga
  roles:
  - icinga2-scripts
    icinga2_needs_notification_scripts: true
```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

## Author Information

- [Janne Heß](https://github.com/dasJ)
