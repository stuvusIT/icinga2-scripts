# icinga2-scripts

This role installs commonly used scripts for Icinga 2.

Currently, the following scripts are installed:

- `check_jenkins` - Checks a Jenkins instance via the [Metrics plugin](https://wiki.jenkins.io/display/JENKINS/Metrics+Plugin).
- `check_kernel` - Checks if the machine needs to be rebooted in order to apply a kernel update.
- `check_services` - Checks if any systemd services failed (systemctl --failed).
- `check_tty` - Checks if a TTY is idling for a long time.
- `check_unifi` - Checks if all APs in a Unifi controller are reachable and up to date.
- `notify_host_mattermost` - Notifies a host state in a Mattermost channel.
- `notify_service_mattermost` - Notifies a service state in a Mattermost channel.

## Requirements

Ubuntu

## Role Variables

| Name                                 | Default/Required         | Description                                         |
|--------------------------------------|:------------------------:|-----------------------------------------------------|
| `icinga2_scripts_path`               | `/usr/lib/stuvus/icinga` | Path where the scripts are installed to             |
| `icinga2_needs_notification_scripts` | `false`                  | Whether to install the notification scripts as well |

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
