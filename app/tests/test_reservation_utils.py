from app.models.reservation import Reservation
from app.models.reservation_utils import *


def test_get_available_slots_one_table_no_slots_any_date():
    assert get_available_slots([
        Reservation(timestamp=dt.datetime(2022, 7, 26, 19)),
        Reservation(timestamp=dt.datetime(2022, 7, 26, 15)),
        Reservation(timestamp=dt.datetime(2022, 7, 26, 17)),
        Reservation(timestamp=dt.datetime(2022, 7, 26, 21)),
        Reservation(timestamp=dt.datetime(2022, 7, 26, 13)),
        Reservation(timestamp=dt.datetime(2022, 7, 26, 11))
    ], dt.datetime(2022, 7, 26), 1) == []


def test_get_available_slots_two_consequetive_reservations_two_tables_any_day():
    date = dt.datetime(2022, 7, 26)
    assert get_available_slots([
        Reservation(timestamp=dt.datetime(2022, 7, 26, 12)),
        Reservation(timestamp=dt.datetime(2022, 7, 26, 10))], date, 2) == [
               dt.datetime(2022, 7, 26, 10, 0),
               dt.datetime(2022, 7, 26, 11, 0),
               dt.datetime(2022, 7, 26, 12, 0),
               dt.datetime(2022, 7, 26, 13, 0),
               dt.datetime(2022, 7, 26, 14, 0),
               dt.datetime(2022, 7, 26, 15, 0),
               dt.datetime(2022, 7, 26, 16, 0),
               dt.datetime(2022, 7, 26, 17, 0),
               dt.datetime(2022, 7, 26, 18, 0),
               dt.datetime(2022, 7, 26, 19, 0),
               dt.datetime(2022, 7, 26, 20, 0),
               dt.datetime(2022, 7, 26, 21, 0)]


def test_get_available_slots_two_consequetive_reservations_one_table_any_day():
    date = dt.datetime(2022, 7, 26)
    assert get_available_slots([
        Reservation(timestamp=dt.datetime(2022, 7, 26, 12)),
        Reservation(timestamp=dt.datetime(2022, 7, 26, 10))], date, 1) \
           == [
               dt.datetime(2022, 7, 26, 14, 0),
               dt.datetime(2022, 7, 26, 15, 0),
               dt.datetime(2022, 7, 26, 16, 0),
               dt.datetime(2022, 7, 26, 17, 0),
               dt.datetime(2022, 7, 26, 18, 0),
               dt.datetime(2022, 7, 26, 19, 0),
               dt.datetime(2022, 7, 26, 20, 0),
               dt.datetime(2022, 7, 26, 21, 0)
           ]


def test_get_available_slots_before_opening_hours_any_day():
    assert get_available_slots([
        Reservation(timestamp=dt.datetime(2022, 7, 27, 11))
    ], dt.datetime(2022, 7, 27, 5), 1) == [
               dt.datetime(2022, 7, 27, 13, 0),
               dt.datetime(2022, 7, 27, 14, 0),
               dt.datetime(2022, 7, 27, 15, 0),
               dt.datetime(2022, 7, 27, 16, 0),
               dt.datetime(2022, 7, 27, 17, 0),
               dt.datetime(2022, 7, 27, 18, 0),
               dt.datetime(2022, 7, 27, 19, 0),
               dt.datetime(2022, 7, 27, 20, 0),
               dt.datetime(2022, 7, 27, 21, 0)
           ]


def test_get_available_slots_today_one_table():
    # reservation should be at the current hour,next available slot should be in 2hrs (not in 1 hr)
    assert get_available_slots([
        Reservation(timestamp=dt.datetime(2022, 7, 28, 15))
    ], dt.datetime.now(), 1) == [
               dt.datetime(2022, 7, 28, 17, 0),
               dt.datetime(2022, 7, 28, 18, 0),
               dt.datetime(2022, 7, 28, 19, 0),
               dt.datetime(2022, 7, 28, 20, 0),
               dt.datetime(2022, 7, 28, 21, 0), ]


def test_get_available_slots_today_multiple_tables():
    # for today reservations next available slot should show the next hour(if available),
    # not the current hour
    assert get_available_slots([
        Reservation(timestamp=dt.datetime(2022, 7, 28, 14)),
        Reservation(timestamp=dt.datetime(2022, 7, 28, 14)),
        Reservation(timestamp=dt.datetime(2022, 7, 28, 16))], dt.datetime.now(),
        2) == [
               dt.datetime(2022, 7, 28, 16, 0),
               dt.datetime(2022, 7, 28, 17, 0),
               dt.datetime(2022, 7, 28, 18, 0),
               dt.datetime(2022, 7, 28, 19, 0),
               dt.datetime(2022, 7, 28, 20, 0),
               dt.datetime(2022, 7, 28, 21, 0)]
