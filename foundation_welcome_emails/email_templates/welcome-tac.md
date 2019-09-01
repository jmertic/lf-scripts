{%- if foundation['tac']['type'] == 'tac' -%}
{%- assign tac = "TAC" -%}
{%- elsif foundation['tac']['type'] == 'tsc' -%}
{%- assign tac = "TSC" -%}
{%- endif -%}
Welcome to the {{ foundation['name'] }} technical community email list.

Here are some great ways get you better engaged in the technical community...

- Learn more about the role of the {{tac}} at {{foundation['tac']['repo_url']}}
- Participate in upcoming meetings on the {{ foundation['name'] }} calendar at {{foundation['groups_io']}}/calendar.
{%- if foundation['slack_url'] != 'None' -%}
- Join the {{ foundation['name'] }} Slack channel at {{foundation['slack_url']}}.
{%- endif -%}
{%- if foundation['forums_url'] != 'None' -%}
- Visit the community forums at foundation['forums_url'] to get more involved in the community.
{%- endif -%}
- Introduce yourself to the group to let everyone know your interests in the technical work at the {{ foundation['name'] }}
{% if foundation['survey']['community']['welcome'] != 'None' %}
If you have a moment, we'd love you to complete our new community member survey so we can ensure the project is serving you well. You can complete the short survey at {{foundation['survey']['community']['welcomne']}}.
{% endif %}
Thanks again for joining the mailing list!

{{ foundation['name'] }} community
