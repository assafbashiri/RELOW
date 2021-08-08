from enum import Enum


class OfferStatus(Enum):

    NOT_EXPIRED_UNCOMPLETED = 1
    EXPIRED_UNCOMPLETED = 2
    NOT_EXPIRED_COMPLETED = 3
    EXPIRED_COMPLETED = 4