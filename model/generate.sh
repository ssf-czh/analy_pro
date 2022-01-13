#!/bin/bash
echo -n 'template_file_base64 = """' > template.py
base64 template.xlsx >> template.py
echo '"""' >> template.py
