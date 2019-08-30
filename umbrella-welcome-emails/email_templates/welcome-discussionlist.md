Welcome to {{ project['name'] }}, hosted by {{ foundation['name'] }}. The email list is for discussion about the project, including questions on usage and code development.

Here are some ways you can get engaged in {{ project['name'] }}...

- Learn more about {{ project['name'] }} at {{ project['homepage_url'] }}
- Get the code at {{ project['repo_url']}}
- Join the regular community meetings that are scheduled on the project calendar at {{ foundation['groups_io'] }}/g/{{ project['mailing_lists']['dev'] }}/calendar.
{%- if project['slack_url'] != 'None' -%}
- Connect with us on Slack at {{ project['slack_url'] }}
{%- elsif foundation['slack_url'] != 'None' -%}
- Find us on the {{ foundation['name'] }} Slack ( {{ foundation['slack_url'] }} ) in channel #{{ project['slack_channel'] }} )
{%- endif -%}

If you are new to this project, feel free to introduce yourself and talk about how you plan to use {{ project['name'] }}.

Thank you!

{{ project['name'] }} Community
