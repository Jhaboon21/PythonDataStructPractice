def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if type(day_of_week) is int:
        if day_of_week-1 > len(days) or day_of_week == 0:
            return None
        return days[day_of_week-1]

weekday_name(9)
weekday_name(1)
weekday_name(0)