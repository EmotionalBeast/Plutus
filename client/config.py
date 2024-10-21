

class Config:
    JOBS = [
        {
            'id': 'volume_monitor',
            'func': 'client.task:volume_monitor',
            'args': (),
            'trigger': 'cron',
            'day_of_week': 'mon-fri',
            'hour': '18',
            'minute': '0',
        }
    ]

    SCHEDULED_API_ENABLED = True