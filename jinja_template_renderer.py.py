from jinja2 import Template
import json

def main():
    renndered_content = None

    # Read template file
    with open("values.j2", "r") as template_file:
        template_content = template_file.read()

        # Load template file
        template = Template(template_content)

        # Read data from bob
        with open("values/values_bob.json", "r") as file:
            data = file.read()
            
            data_contet = json.loads(data)

            # Render bob data into template
            rendered_content = template.render(data_contet)

        # Write rendered bob data into output file
        with open("identities/identity_bob.txt", 'w') as output_file:
            output_file.write(rendered_content)
    
        # Repeat for Alice
        with open("values/values_alice.json", "r") as file:
            data = file.read()
            
            data_contet = json.loads(data)

            rendered_content = template.render(data_contet)

        with open("identities/identity_alice.txt", 'w') as output_file:
            output_file.write(rendered_content)
    
if __name__ == "__main__":
    main()