from enum import IntEnum, _simple_enum  # type: ignore
from typing import Any, Optional, Type, Union


@_simple_enum(IntEnum)
class ResultStatus:
    value: int
    _value_: int
    phrase: str
    description: str

    def __new__(cls, value: int, phrase: str='', description: str=''):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.phrase = phrase
        obj.description = description
        return obj

    # OK = 200, 'OK', 'Success'
    SUCCESS = 200, 'Success', 'Success'
    FAILURE = 400, 'Failure'
    CREATED = 201, 'Created'
    NOT_FOUND = 404, 'Not Found'
    NOT_IMPLEMENTED = 501, 'Not Implemented'
    DATABASE_ERROR = 600, 'Database Error'


class BaseResponse(dict):
    STATUS: Type[ResultStatus] = ResultStatus
    __slots__ = (
        'code',
        'msg',
        'data',
    )
    def __new__(cls, *args: Any, **kwargs: Any):
        is_valid_kwargs = set(kwargs.keys()).issubset(cls.__slots__)
        # print('__new__', cls, args, kwargs, is_valid_kwargs)
        if not is_valid_kwargs:
            raise KeyError(f'{cls} only accept kwargs: {cls.__slots__}. Got: {args}, {kwargs}')
        return super().__new__(cls, *args, **kwargs)

    def __init__(
        self, *args: Any,
        code: int=200,
        msg: Optional[Union[str, Exception]]=None,
        data: Optional[Any]=None, **kwargs: Any,
    ):
        code, msg, data = self.check_kwargs(code, msg, data)
        super().__init__(code=code, msg=msg, data=data)
        for attr in self.__slots__:
            setattr(self, attr, self.get(attr, None))

    def __setitem__(self, key: str, val: Any):
        if not self.__slots__.__contains__(key):
            raise KeyError(f"'{self.__class__.__name__}' object has not allowed attribute '{key}'")
        super().__setitem__(key, val)

    def __eq__(self, __value: object) -> bool:
        return __value in self.values()

    def check_kwargs(self,
        code: Union[int, ResultStatus]=200,
        msg: Optional[str]=None,
        data: Optional[Any]=None, ):
        if not isinstance(code, ResultStatus):
            code = self.STATUS(code)
        msg = msg or code.phrase
        return code, msg, data


class Result(BaseResponse):
    """API general response class.

    e.g.
        response = Result()
        response = Result(code=100)
        Result(code=100, msg='Hello', data={'a': 1, 'b': 2})
        print(response)
    """
    pass


class Response(BaseResponse):

    def check_kwargs(self,
        code: Union[int, ResultStatus]=200,
        msg: Optional[str]=None,
        data: Optional[Any]=None, ):
        code, msg, data = super().check_kwargs(code, msg, data)
        if not isinstance(data, (dict, list)):
            raise TypeError(f'{self.__class__} data must be dict or list. Got: {type(data)}')
        return code, msg, data


if __name__ == "__main__":
    assert 200 in ResultStatus.__members__.values()
    print(getattr(ResultStatus, 'SUCCESS'))
    assert ResultStatus.SUCCESS == 200
    assert ResultStatus.SUCCESS.value == 200
    assert ResultStatus.SUCCESS.phrase == 'Success'
    print(ResultStatus.SUCCESS.description)
    assert ResultStatus.SUCCESS.description == 'Success'
    _ = ResultStatus(200)
    # _ = ResultStatus(200, phrase='abc')
    assert _ == ResultStatus.SUCCESS
    assert _ == 200
    assert _ == ResultStatus.SUCCESS.value
    assert _.value == 200
    print(_.phrase, _.description)
    assert _.phrase == 'Success'
    assert _.description == 'Success'
    print(type(_), _, _.phrase, _.description)
    # assert ResultStatus.get_by_value(200) == ResultStatus.OK

    # response = Result()
    response = Result(
        code=600, msg='abc',
        # dd=1,
    )
    # response = Result(code=100, msg='Hello', data={'a': 1, 'b': 2})
    response['data'] = {'c': 1, 'd': 2}
    print(response)
