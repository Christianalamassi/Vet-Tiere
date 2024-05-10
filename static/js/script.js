< script >
    CronofyElements.DateTimePicker({
        element_token: "{ELEMENT_TOKEN}",
        target_id: "cronofy-date-time-picker",
        availability_query: {
            participants: [{
                required: "all",
                members: [{
                        sub: "acc_5ba21743f408617d1269ea1e"
                    },
                    {
                        sub: "acc_64b17d868090ea21640c914c"
                    }
                ]
            }],
            required_duration: {
                minutes: 30
            },
            query_periods: [{
                    start: "2024-05-10T09:00:00Z",
                    end: "2024-05-10T17:00:00Z"
                },
                {
                    start: "2024-05-11T09:00:00Z",
                    end: "2024-05-11T17:00:00Z"
                }
            ]
        },
        styles: {
            prefix: "custom-name"
        },
        callback: notification => console.log("callback", notification)
    }); <
/script>