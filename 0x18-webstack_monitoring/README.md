* Adding your API key to the Datadog Agent configuration: /etc/datadog-agent/datadog.yaml


* Setting SITE in the Datadog Agent configuration: /etc/datadog-agent/datadog.yaml

/usr/bin/systemctl
* Starting the Datadog Agent..

DD_API_KEY=1cc4793d8087d3c831af550a7369e82e DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script_agent7.sh)"
