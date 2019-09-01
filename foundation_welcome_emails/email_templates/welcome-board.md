{%- if foundation['board']['type'] == 'gb' -%}
{%- assign gb = "Governing Board" -%}
{%- assign gb_members = "Governing Board members" -%}
{%- elsif foundation['board']['type'] == 'bod' -%}
{%- assign gb = "Board of Directors" -%}
{%- assign gb_members = "Board Directors" -%}
{%- endif -%}
Welcome to the {{ foundation['name'] }} {{gb}}. This email list is for private communication amongst {{ foundation['name'] }} {{gb_members}} and project staff. Please ensure that {{foundation['mailing_lists']['board']}}{{foundation['groups_io_email']}} is whitelisted in your email spam blocker to prevent missed notices.

To get up to speed on serving on the {{gb}}, please complete the following:

- Make sure the {{gb}} meetings are on your calendar. You can review all meetings and events of the {{gb}} at {{foundation['groups_io']}}/calendar.
- To have your headshot and bio on the {{ foundation['name'] }} website at {{foundation['board']['homepage_url']}}, please email {{foundation['mailing_lists']['staff']}}{{foundation['groups_io_email']}} with your headshot and bio.
- Learn more about the {{gb}} and past actions in the board portal at {{foundation['groups_io']}}/g/{{foundation['mailing_lists']['board']}}/wiki.

Thank you for your service on the {{gb}}!

{{ foundation['name'] }} staff
