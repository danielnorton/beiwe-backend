import json

from deployment_helpers.constants import ELASTICBEANSTALK_CONFIGURATION_FILE, BEIWE_ENVIRONMENT_FILE


class AutogeneratedParameter(Exception): pass


"https://github.com/onnela-lab/beiwe-backend/archive/master.zip"

with open(BEIWE_ENVIRONMENT_FILE, 'r') as f:
    # read in the json, transform it into a comma separated list of parameters.
    environment_variables = ",".join(["%s=%s" % (k,v) for k,v in json.load(f).items()])

with open(ELASTICBEANSTALK_CONFIGURATION_FILE, 'r') as f:
    eb_configuration = json.load(f)

configuration = [
    
    # Instance launch configuration details
    {
        'Namespace': 'aws:autoscaling:launchconfiguration',
        'OptionName': 'InstanceType',
        'Value': 't2.medium'
    },
    {
        'Namespace': 'aws:autoscaling:launchconfiguration',
        'OptionName': 'IamInstanceProfile',
        'Value': AutogeneratedParameter("IamInstanceProfile")
    },
    {
        'Namespace': 'aws:autoscaling:launchconfiguration',
        'OptionName': 'EC2KeyName',
        'Value': 'ohio-test-key'
    },
    # {
    #     'Namespace': 'aws:autoscaling:launchconfiguration',
    #     'OptionName': 'ImageId',
    #     'Value': 'ami-5c00ef26'
    # },
    # {
    #     'Namespace': 'aws:autoscaling:launchconfiguration',
    #     'OptionName': 'SecurityGroups',
    #     'Value': 'sg-3e2d2758,sg-a47162d9'
    # },
    
    
    # {
    #     'Namespace': 'aws:autoscaling:launchconfiguration',
    #     'OptionName': 'BlockDeviceMappings',
    # }, {
    #     'Namespace': 'aws:autoscaling:launchconfiguration',
    #     'OptionName': 'MonitoringInterval',
    #     'Value': '1 minute'
    # }, {
    #     'Namespace': 'aws:autoscaling:launchconfiguration',
    #     'OptionName': 'RootVolumeIOPS',
    # },
    {   # using the default value of 8
        'Namespace': 'aws:autoscaling:launchconfiguration',
        'OptionName': 'RootVolumeSize',
        'Value': 8
    },
    #  {
    #     'Namespace': 'aws:autoscaling:launchconfiguration',
    #     'OptionName': 'RootVolumeType',
    #     # 'Value': "gp2",
    # },
    {
        'Namespace': 'aws:autoscaling:launchconfiguration',
        'OptionName': 'SSHSourceRestriction',
        'Value': 'tcp,22,22,0.0.0.0/0'
    },
    
    # cloudwatch alarms
    {
        'Namespace': 'aws:autoscaling:trigger',
        'OptionName': 'BreachDuration',
        'Value': '1'
    }, {
        'Namespace': 'aws:autoscaling:trigger',
        'OptionName': 'EvaluationPeriods',
        'Value': '1'
    },
    
    # environment variables
    {
        'Namespace': 'aws:cloudformation:template:parameter',
        'OptionName': 'EnvironmentVariables',
        'Value': environment_variables,
    },
    
    # template settincs
    {
        'Namespace': 'aws:cloudformation:template:parameter',
        'OptionName': 'AppSource',
        'Value': 'http://s3.amazonaws.com/elasticbeanstalk-samples-us-east-1/python-sample-20150402.zip'
    }, {
        'Namespace': 'aws:cloudformation:template:parameter',
        'OptionName': 'HooksPkgUrl',
        'Value': 'https://s3.dualstack.us-east-1.amazonaws.com/elasticbeanstalk-env-resources-us-east-1/stalks/eb_python_4.0.1.95.6/lib/hooks.tar.gz'
    }, {
        'Namespace': 'aws:cloudformation:template:parameter',
        'OptionName': 'InstancePort',
        'Value': '80'
    },
    
    # deployment network details
    # {
    #     'Namespace': 'aws:ec2:vpc',
    #     'OptionName': 'VPCId',
    #     'Value': 'vpc-c6e16da2'
    # },
    # {
    #     'Namespace': 'aws:ec2:vpc',
    #     'OptionName': 'ELBSubnets',
    #     'Value': 'subnet-10718a66,subnet-ea9599c1,subnet-8018a9bd,subnet-bf1f02e6'
    # },
    # {
    #     'Namespace': 'aws:ec2:vpc',
    #     'OptionName': 'Subnets',
    #     'Value': 'subnet-10718a66,subnet-ea9599c1,subnet-8018a9bd,subnet-bf1f02e6'
    # },
    
    # static network details
    # {   # todo: not in a vpc?
    #     'Namespace': 'aws:ec2:vpc',
    #     'OptionName': 'AssociatePublicIpAddress',
    #     'Value': 'true'
    # },
    {
        'Namespace': 'aws:ec2:vpc',
        'OptionName': 'ELBScheme',
        'Value': 'public'
    }, {
        'Namespace': 'aws:elasticbeanstalk:application',
        'OptionName': 'Application Healthcheck URL',
        'Value': ''
    },
    # autoscaling settings
    {
        'Namespace': 'aws:autoscaling:asg',
        'OptionName': 'Availability Zones',
        'Value': 'Any'
    }, {
        'Namespace': 'aws:autoscaling:asg',
        'OptionName': 'Cooldown',
        'Value': '360'
    }, {
        'Namespace': 'aws:autoscaling:asg',
        'OptionName': 'Custom Availability Zones',
        'Value': ''
    }, {
        'Namespace': 'aws:autoscaling:asg',
        'OptionName': 'MaxSize',
        'Value': '2'
    }, {
        'Namespace': 'aws:autoscaling:asg',
        'OptionName': 'MinSize',
        'Value': '1'
    }, {
        'Namespace': 'aws:autoscaling:trigger',
        'OptionName': 'LowerBreachScaleIncrement',
        'Value': '-1'
    }, {
        'Namespace': 'aws:autoscaling:trigger',
        'OptionName': 'LowerThreshold',
        'Value': '20'
    }, {
        'Namespace': 'aws:autoscaling:trigger',
        'OptionName': 'MeasureName',
        'Value': 'CPUUtilization'
    }, {
        'Namespace': 'aws:autoscaling:trigger',
        'OptionName': 'Period',
        'Value': '1'
    }, {
        'Namespace': 'aws:autoscaling:trigger',
        'OptionName': 'Statistic',
        'Value': 'Maximum'
    }, {
        'Namespace': 'aws:autoscaling:trigger',
        'OptionName': 'Unit',
        'Value': 'Percent'
    }, {
        'Namespace': 'aws:autoscaling:trigger',
        'OptionName': 'UpperBreachScaleIncrement',
        'Value': '1'
    }, {
        'Namespace': 'aws:autoscaling:trigger',
        'OptionName': 'UpperThreshold',
        'Value': '85'
    }, {
        'Namespace': 'aws:autoscaling:updatepolicy:rollingupdate',
        'OptionName': 'MaxBatchSize',
        'Value': '1'
    }, {
        'Namespace': 'aws:autoscaling:updatepolicy:rollingupdate',
        'OptionName': 'MinInstancesInService',
        'Value': '1'
    },
    # {
    #     'Namespace': 'aws:autoscaling:updatepolicy:rollingupdate',
    #     'OptionName': 'PauseTime',
    # },
    {
        'Namespace': 'aws:autoscaling:updatepolicy:rollingupdate',
        'OptionName': 'RollingUpdateEnabled',
        'Value': 'true'
    }, {
        'Namespace': 'aws:autoscaling:updatepolicy:rollingupdate',
        'OptionName': 'RollingUpdateType',
        'Value': 'Health'
    }, {
        'Namespace': 'aws:autoscaling:updatepolicy:rollingupdate',
        'OptionName': 'Timeout',
        'Value': 'PT30M'
    },
    
    # Logging settings
    {
        'Namespace': 'aws:elasticbeanstalk:cloudwatch:logs',
        'OptionName': 'DeleteOnTerminate',
        'Value': 'false'
    }, {
        'Namespace': 'aws:elasticbeanstalk:cloudwatch:logs',
        'OptionName': 'RetentionInDays',
        'Value': '7'
    }, {
        'Namespace': 'aws:elasticbeanstalk:cloudwatch:logs',
        'OptionName': 'StreamLogs',
        'Value': 'false'
    },
    
    # miscellaneous EB configuration
    {
        'Namespace': 'aws:elasticbeanstalk:command',
        'OptionName': 'BatchSize',
        'Value': '30'
    }, {
        'Namespace': 'aws:elasticbeanstalk:command',
        'OptionName': 'BatchSizeType',
        'Value': 'Percentage'
    }, {
        'Namespace': 'aws:elasticbeanstalk:command',
        'OptionName': 'DeploymentPolicy',
        'Value': 'Rolling'
    }, {
        'Namespace': 'aws:elasticbeanstalk:command',
        'OptionName': 'IgnoreHealthCheck',
        'Value': 'false'
    }, { # Time at which a timeout occurs after deploying the environment
        'Namespace': 'aws:elasticbeanstalk:command',
        'OptionName': 'Timeout',
        'Value': '300'
    }, {
        'Namespace': 'aws:elasticbeanstalk:control',
        'OptionName': 'DefaultSSHPort',
        'Value': '22'
    }, {'Namespace': 'aws:elasticbeanstalk:control',
        'OptionName': 'LaunchTimeout',
        'Value': '0'
    }, {
        'Namespace': 'aws:elasticbeanstalk:control',
        'OptionName': 'LaunchType',
        'Value': 'Migration'
    }, {
        'Namespace': 'aws:elasticbeanstalk:control',
        'OptionName': 'RollbackLaunchOnFailure',
        'Value': 'false'
    },
    
    # Python environment configuration
    {
        'Namespace': 'aws:elasticbeanstalk:container:python',
        'OptionName': 'NumProcesses',
        'Value': '2'
    }, {
        'Namespace': 'aws:elasticbeanstalk:container:python',
        'OptionName': 'NumThreads',
        'Value': '20'
    }, {
        'Namespace': 'aws:elasticbeanstalk:container:python',
        'OptionName': 'StaticFiles',
        'Value': '/static/=frontend/static/'
    }, {
        'Namespace': 'aws:elasticbeanstalk:container:python',
        'OptionName': 'WSGIPath',
        'Value': 'wsgi.py'
    }, {
        'Namespace': 'aws:elasticbeanstalk:container:python:staticfiles',
        'OptionName': '/static/',
        'Value': 'frontend/static/'
    },
    
    # EB roles and permissions
    {
        'Namespace': 'aws:elasticbeanstalk:environment',
        'OptionName': 'EnvironmentType',
        'Value': 'LoadBalanced'
    },
    # {
    #     'Namespace': 'aws:elasticbeanstalk:environment',
    #     'OptionName': 'ExternalExtensionsS3Bucket'
    # }, {
    #     'Namespace': 'aws:elasticbeanstalk:environment',
    #     'OptionName': 'ExternalExtensionsS3Key'
    # },
    {
        'Namespace': 'aws:elasticbeanstalk:environment',
        'OptionName': 'LoadBalancerType',
        'Value': 'classic'
    }, {
        'Namespace': 'aws:elasticbeanstalk:environment',
        'OptionName': 'ServiceRole',
        'Value': AutogeneratedParameter("ServiceRole")
    },
    
    # Health check/Reporting details
    {
        'Namespace': 'aws:elasticbeanstalk:healthreporting:system',
        'OptionName': 'ConfigDocument',
        'Value': '{"Version":1,"CloudWatchMetrics":{"Instance":{"CPUIrq":null,"LoadAverage5min":null,"ApplicationRequests5xx":null,"ApplicationRequests4xx":null,"CPUUser":null,"LoadAverage1min":null,"ApplicationLatencyP50":null,"CPUIdle":null,"InstanceHealth":null,"ApplicationLatencyP95":null,"ApplicationLatencyP85":null,"RootFilesystemUtil":null,"ApplicationLatencyP90":null,"CPUSystem":null,"ApplicationLatencyP75":null,"CPUSoftirq":null,"ApplicationLatencyP10":null,"ApplicationLatencyP99":null,"ApplicationRequestsTotal":null,"ApplicationLatencyP99.9":null,"ApplicationRequests3xx":null,"ApplicationRequests2xx":null,"CPUIowait":null,"CPUNice":null},"Environment":{"InstancesSevere":null,"InstancesDegraded":null,"ApplicationRequests5xx":null,"ApplicationRequests4xx":null,"ApplicationLatencyP50":null,"ApplicationLatencyP95":null,"ApplicationLatencyP85":null,"InstancesUnknown":null,"ApplicationLatencyP90":null,"InstancesInfo":null,"InstancesPending":null,"ApplicationLatencyP75":null,"ApplicationLatencyP10":null,"ApplicationLatencyP99":null,"ApplicationRequestsTotal":null,"InstancesNoData":null,"ApplicationLatencyP99.9":null,"ApplicationRequests3xx":null,"ApplicationRequests2xx":null,"InstancesOk":null,"InstancesWarning":null}}}'
    }, {
        'Namespace': 'aws:elasticbeanstalk:healthreporting:system',
        'OptionName': 'HealthCheckSuccessThreshold',
        'Value': 'Ok'
    }, {
        'Namespace': 'aws:elasticbeanstalk:healthreporting:system',
        'OptionName': 'SystemType',
        'Value': 'enhanced'
    }, {
        'Namespace': 'aws:elasticbeanstalk:hostmanager',
        'OptionName': 'LogPublicationControl',
        'Value': 'false'
    }, {
        'Namespace': 'aws:elasticbeanstalk:managedactions',
        'OptionName': 'ManagedActionsEnabled',
        'Value': 'false'
    },
    # {
    #     'Namespace': 'aws:elasticbeanstalk:managedactions',
    #     'OptionName': 'PreferredStartTime'
    # },
    {
        'Namespace': 'aws:elasticbeanstalk:managedactions:platformupdate',
        'OptionName': 'InstanceRefreshEnabled',
        'Value': 'false'
    },
    # {
    #     'Namespace': 'aws:elasticbeanstalk:managedactions:platformupdate',
    #     'OptionName': 'UpdateLevel'
    # },
    {
        'Namespace': 'aws:elasticbeanstalk:monitoring',
        'OptionName': 'Automatically Terminate Unhealthy Instances',
        'Value': 'true'
    }, {
        'Namespace': 'aws:elb:healthcheck',
        'OptionName': 'HealthyThreshold',
        'Value': '3'
    }, {
        'Namespace': 'aws:elb:healthcheck',
        'OptionName': 'Interval',
        'Value': '10'
    }, {
        'Namespace': 'aws:elb:healthcheck',
        'OptionName': 'Target',
        'Value': 'TCP:80'
    }, {
        'Namespace': 'aws:elb:healthcheck',
        'OptionName': 'Timeout',
        'Value': '5'
    }, {
        'Namespace': 'aws:elb:healthcheck',
        'OptionName': 'UnhealthyThreshold',
        'Value': '5'
    },
    
    # Notification
    {   # These settings generate an SNS instance for the system
        'Namespace': 'aws:elasticbeanstalk:sns:topics',
        'OptionName': 'Notification Endpoint',
        'Value': 'eli@zagaran.com'
    }, {
        'Namespace': 'aws:elasticbeanstalk:sns:topics',
        'OptionName': 'Notification Protocol',
        'Value': 'email'
    },
    # { #TODO: autogenerated?
    #     'Namespace': 'aws:elasticbeanstalk:sns:topics',
    #     'OptionName': 'Notification Topic ARN',
    #     'Value': 'arn:aws:sns:us-east-1:284616134063:ElasticBeanstalkNotifications-Environment-beiweCluster-staging'
    # },
    # {
    #     'Namespace': 'aws:elasticbeanstalk:sns:topics',
    #     'OptionName': 'Notification Topic Name'
    # },
    
    # # Load Balancer configuration
    # {
    #     'Namespace': 'aws:elb:loadbalancer',
    #     'OptionName': 'SecurityGroups',
    #     'Value': 'sg-e271629f'
    # },
    #
    # {
    #     'Namespace': 'aws:elb:listener:80',
    #     'OptionName': 'InstancePort',
    #     'Value': '80'
    # }, {
    #     'Namespace': 'aws:elb:listener:80',
    #     'OptionName': 'InstanceProtocol',
    #     'Value': 'HTTP'
    # }, {
    #     'Namespace': 'aws:elb:listener:80',
    #     'OptionName': 'ListenerEnabled',
    #     'Value': 'true'
    # }, {
    #     'Namespace': 'aws:elb:listener:80',
    #     'OptionName': 'ListenerProtocol',
    #     'Value': 'HTTP'
    # }, {
    #     'Namespace': 'aws:elb:listener:80',
    #     'OptionName': 'PolicyNames',
    # }, {
    #     'Namespace': 'aws:elb:listener:80',
    #     'OptionName': 'SSLCertificateId',
    # }, {
    #     'Namespace': 'aws:elb:loadbalancer',
    #     'OptionName': 'CrossZone',
    #     'Value': 'true'
    # }, {
    #     'Namespace': 'aws:elb:loadbalancer',
    #     'OptionName': 'LoadBalancerHTTPPort',
    #     'Value': '80'
    # }, {
    #     'Namespace': 'aws:elb:loadbalancer',
    #     'OptionName': 'LoadBalancerHTTPSPort',
    #     'Value': 'OFF'
    # }, {
    #     'Namespace': 'aws:elb:loadbalancer',
    #     'OptionName': 'LoadBalancerPortProtocol',
    #     'Value': 'HTTP'
    # }, {
    #     'Namespace': 'aws:elb:loadbalancer',
    #     'OptionName': 'LoadBalancerSSLPortProtocol',
    #     'Value': 'HTTPS'
    # }, {
    #     'Namespace': 'aws:elb:loadbalancer',
    #     'OptionName': 'SSLCertificateId',
    # }, {
    #     'Namespace': 'aws:elb:policies',
    #     'OptionName': 'ConnectionDrainingEnabled',
    #     'Value': 'true'
    # }, {
    #     'Namespace': 'aws:elb:policies',
    #     'OptionName': 'ConnectionDrainingTimeout',
    #     'Value': '20'
    # }, {
    #     'Namespace': 'aws:elb:policies',
    #     'OptionName': 'ConnectionSettingIdleTimeout',
    #     'Value': '60'
    # },
    #
    # Totally irrelevant details
    #     {
    #         'Namespace': 'aws:elasticbeanstalk:xray',
    #         'OptionName': 'XRayEnabled',
    #         'Value': 'false'
    #     },
]