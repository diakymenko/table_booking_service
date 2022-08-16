import datetime as dt


def get_available_slots(reservations, date, tables):
    print(reservations)

    start = 10  # #default opening/closing hours for all restaurants
    end = 23
    current_date = dt.datetime.now()

    potential_slots = []  # list of datetime obj
    for i in range(start, end - 1):  # since we allow 2 hrs for 1 reservation,
        # the last possible time for reservation will be 21:00
        potential_slots.append(dt.datetime(date.year, date.month, date.day, i))

    dict_booked_timeslots = {}
    for slot in potential_slots:
        dict_booked_timeslots[slot.hour] = dict_booked_timeslots.get(slot.hour,
                                                                     0)

    set_booked_slots = set()
    # list of Reservation objects
    for reservation in reservations:
        if reservation.timestamp.hour in dict_booked_timeslots:
            dict_booked_timeslots[reservation.timestamp.hour] += 1
            set_booked_slots.add(reservation.timestamp.hour)

    # This code makes sure we do not use our table(reservation) 1hr prior and 1hr later
    # the booking.

    for key, value in dict_booked_timeslots.items():
        if key in set_booked_slots:
            if key - 1 in dict_booked_timeslots:
                if dict_booked_timeslots[key - 1] < value:
                    dict_booked_timeslots[key - 1] = value
            if key + 1 in dict_booked_timeslots:
                if dict_booked_timeslots[key + 1] < value:
                    dict_booked_timeslots[key + 1] = value

    res = []
    for key, value in dict_booked_timeslots.items():
        if value < tables:
            if date.day == current_date.day:
                if key > current_date.hour:
                    res.append(
                        dt.datetime(date.year, date.month, date.day, key))
            else:
                res.append(dt.datetime(date.year, date.month, date.day, key))

    return res
