source scrapy.env/bin/activate

export PYTHONPATH=`pwd`/app

CONFIG_MODE_TEXT=`cat $PYTHONPATH/app/config/config_mode`

# alias supervisorctl="supervisorctl -c $PYTHONPATH/app/config/$CONFIG_MODE_TEXT/supervisord.conf"

# alias supervilord="supervisord -c $PYTHONPATH/app/config/$CONFIG_MODE_TEXT/supervisord.conf"

sudo ln -s -f $PYTHONPATH/app/config/$CONFIG_MODE_TEXT/supervisord.conf etc/supervisord.conf
