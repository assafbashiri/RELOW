from enum import Enum


class OfferStatus(Enum):

    ACTIVE = 1
    DONE = 2
    CANCELED_BY_SELLER = 3
    CANCELED_BY_BUYER = 4
    EXPIRED_ZERO_BUYERS = 5


