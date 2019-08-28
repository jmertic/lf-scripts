Welcome to the private discussion list for {{ project['name'] }}, hosted by {{ foundation['name'] }}. This channel is for the TSC and project leads to discuss sensitive items such as CoC violations or committer issues. Please direct all other conversation to the public email list at {%- if project['mailing_lists']['dev'] -%}
 {{ foundation['groups_io'] }}/g/{{ project['mailing_lists']['dev'] }}.
{%- elsif project['mailing_lists']['discussion'] -%}
 {{ foundation['groups_io'] }}/g/{{ project['mailing_lists']['discussion'] }}.
{%- endif -%}

Thank you for your leadership with {{ project['name'] }}!

{{ project['name'] }} leadership
