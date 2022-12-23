from typing import Union, List
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass(init=False, repr=False, eq=False)
class Component(ABC):
    @abstractmethod
    def load(self, *args, **kwargs):
        pass


@dataclass(init=False, repr=False, eq=False)
class Reader(Component):
    @abstractmethod
    def __hash__(self) -> int:
        """
        Custom hashing function useful to compare instances of `Reader`.

        Raises:
            NotImplementedError:

        Returns:
            int: hash value
        """
        raise NotImplementedError

    @abstractmethod
    def apply(self, input_texts: List[str], context: List[List[str]], *args, **kwargs):
        pass


@dataclass(init=False, repr=False, eq=False)
class Indexer(Component):
    index_root: str = field(
        metadata={
            "name": "Index root",
            "description": "Path to root directory where index to be stored",
        },
    )
    index_name: str = field(
        metadata={
            "name": "Index name",
        },
    )

    @abstractmethod
    def index(self, collection: Union[List[dict], str], *args, **kwargs):
        pass


@dataclass(init=False, repr=False, eq=False)
class Retriever(Component):
    index_root: str = field(
        metadata={
            "name": "Index root",
            "description": "Path to root directory where index is stored",
        },
    )
    index_name: str = field(
        metadata={
            "name": "Index name",
        },
    )
    collection: str = field(
        metadata={
            "name": "The corpus file split in paragraphs",
        },
    )

    @abstractmethod
    def __hash__(self) -> int:
        """
        Custom hashing function useful to compare instances of `Retriever`.

        Raises:
            NotImplementedError:

        Returns:
            int: hash value
        """
        raise NotImplementedError

    @abstractmethod
    def retrieve(self, input_texts: List[str], *args, **kwargs):
        pass
