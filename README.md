# MCP UP
Start up Mobile Core with ease now!

### Prerequisites
* python 3

### Usage
Clone the repository:
```sh
$ git clone https://github.com/josemigallas/mcp-up.git
```

Or simply download the script:
```sh
$  curl -O https://raw.githubusercontent.com/josemigallas/mcp-up/master/mcp-up.py
```

And finally, at `/mobile-core`, run:
```sh
$ mcp-up.py
```

You might need to flag this file as executable:
```sh
$ chmod u+x mcp-up.py
```

### Tweaks
*mcp-up* will ask you for a DockerHub username and password everytime. However, you can add those to your profile (.bash_profile or equivalent) in order to avoid just that:
```sh
echo '# Global DockerHub credentials:' >>~/.bash_profile
echo 'export DOCKERHUB_USER="username"' >>~/.bash_profile
echo 'export DOCKERHUB_PASS="password"' >>~/.bash_profile
```
