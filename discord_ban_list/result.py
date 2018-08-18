from abc import ABC, abstractproperty, abstractmethod
from typing import Union, Optional


class BanABC(ABC):
    __slots__ = ()

    @abstractproperty
    def user_id(self) -> int:
        pass

    @abstractproperty
    def banned(self) -> bool:
        pass

    @abstractproperty
    def reason(self) -> Optional[str]:
        pass

    @abstractproperty
    def case_id(self) -> Optional[int]:
        pass

    @abstractproperty
    def proof(self) -> Optional[str]:
        pass

    @abstractmethod
    def __eq__(self, other):
        pass


class Ban(BanABC):
    __slots__ = ('_proof', '_user_id', '_case_id', '_reason')

    def __init__(self, user_id: Union[int, str], reason: str, case_id: Union[str, int], proof: str):
        self._user_id = int(user_id)
        self._reason = reason
        self._case_id = int(case_id)
        self._proof = proof

    @property
    def user_id(self) -> Optional[int]:
        return self._user_id

    @property
    def banned(self) -> bool:
        return True

    @property
    def reason(self) -> Optional[str]:
        return self._reason

    @property
    def case_id(self) -> Optional[int]:
        return self._case_id

    @property
    def proof(self) -> Optional[str]:
        return self._proof

    def __str__(self):
        return '<DBan banned: True, User: {user}, Case: {case}, reason: {reason!r}, proof: {proof!r}>'.format(
            user=self.user_id,
            case=self.case_id,
            reason=self.reason,
            proof=self.proof,
        )

    def __eq__(self, other):
        if not isinstance(other, Ban):
            return False
        return other.user_id == self.user_id \
               and other.case_id == self.case_id


class NoBan(BanABC):
    __slots__ = ('_user_id',)

    def __init__(self, user_id: Union[str, int]):
        self._user_id = int(user_id)

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def banned(self) -> bool:
        return False

    @property
    def reason(self) -> Optional[str]:
        return None

    @property
    def case_id(self) -> Optional[int]:
        return None

    @property
    def proof(self) -> Optional[str]:
        return None

    def __str__(self):
        return '<DBan banned: False, User: {user}>'.format(user=self.user_id)

    def __eq__(self, other):
        if not isinstance(other, NoBan):
            return False
        return other.user_id == self.user_id
