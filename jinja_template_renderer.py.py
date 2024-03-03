from jinja2 import Template
import json

def main():
    renndered_content = None

    with open("values.j2", "r") as template_file:
        template_content = template_file.read()

        template = Template(template_content)

        with open("values_bob.json", "r") as file:
            data = file.read()
            
            data_contet = json.loads(data)

            rendered_content = template.render(data_contet)

        with open("identity_bob.txt", 'w') as output_file:
            output_file.write(rendered_content)
    

        with open("values_alice.json", "r") as file:
            data = file.read()
            
            data_contet = json.loads(data)

            rendered_content = template.render(data_contet)

        with open("identity_alice.txt", 'w') as output_file:
            output_file.write(rendered_content)
    
if __name__ == "__main__":
    main()