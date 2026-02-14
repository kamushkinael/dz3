#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            port=dict(type='int', required=True),
            files_path=dict(type='str', required=True),
            dest=dict(type='str', required=True),
        )
    )

    config_content = f"""server {{
    listen {module.params['port']};
    server_name _;
    location /files {{
        alias {module.params['files_path']}/;
        autoindex on;
    }}
}}"""

    with open(module.params['dest'], 'w') as f:
        f.write(config_content)

    module.exit_json(changed=True, msg="Config written")

if __name__ == '__main__':
    main()
