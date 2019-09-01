{%- if foundation['tac']['type'] == 'tac' -%}
{%- assign tac = "TAC" -%}
{%- elsif foundation['tac']['type'] == 'tsc' -%}
{%- assign tac = "TSC" -%}
{%- endif -%}
Welcome to the {{ foundation['name'] }} {{tac}}. This email list is for private discussion amongst {{tac}} voting members only, typically for topics such as votes or sensitive topics.

To get up to speed on serving on the {{tac}}, please complete the following:

- Make sure the {{tac}} meetings are on your calendar. You can review all meetings and events of the {{tac}} at {{foundation['groups_io']}}/calendar.
- To have your headshot and bio on the ASWF website at {{foundation['tac']['homepage_url']}}, please email {{foundation['mailing_lists']['staff']}}{{foundation['groups_io_email']}} with your headshot and bio.
- Review your information at {{foundation['tac']['repo_url']}}/blob/master/README.md, and issue a PR to have your information updated or added.
- Learn more about the {{tac}} processes and policies as well as review past meetings at {{foundation['tac']['repo_url']}}.

Thank you again for your service on the {{ foundation['name'] }} {{tac}}. Feel free to reach out to any of the LF staff for any questions or concerns you have.

{{ foundation['name'] }} {{tac}}
