# 定义100 - 500错误码
class StatusCode(object):

    HTTP_100_CONTINUE = 100
    HTTP_101_SWITCHING_PROTOCOLS = 101
    HTTP_200_OK = 200
    HTTP_201_CREATED = 201
    HTTP_202_ACCEPTED = 202
    HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203
    HTTP_204_NO_CONTENT = 204
    HTTP_205_RESET_CONTENT = 205
    HTTP_206_PARTIAL_CONTENT = 206
    HTTP_207_MULTI_STATUS = 207
    HTTP_208_ALREADY_REPORTED = 208
    HTTP_226_IM_USED = 226
    HTTP_300_MULTIPLE_CHOICES = 300
    HTTP_301_MOVED_PERMANENTLY = 301
    HTTP_302_FOUND = 302
    HTTP_303_SEE_OTHER = 303
    HTTP_304_NOT_MODIFIED = 304
    HTTP_305_USE_PROXY = 305
    HTTP_306_RESERVED = 306
    HTTP_307_TEMPORARY_REDIRECT = 307
    HTTP_308_PERMANENT_REDIRECT = 308
    HTTP_400_BAD_REQUEST = 400
    HTTP_401_UNAUTHORIZED = 401
    HTTP_402_PAYMENT_REQUIRED = 402
    HTTP_403_FORBIDDEN = 403
    HTTP_404_NOT_FOUND = 404
    HTTP_405_METHOD_NOT_ALLOWED = 405
    HTTP_406_NOT_ACCEPTABLE = 406
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407
    HTTP_408_REQUEST_TIMEOUT = 408
    HTTP_409_CONFLICT = 409
    HTTP_410_GONE = 410
    HTTP_411_LENGTH_REQUIRED = 411
    HTTP_412_PRECONDITION_FAILED = 412
    HTTP_413_REQUEST_ENTITY_TOO_LARGE = 413
    HTTP_414_REQUEST_URI_TOO_LONG = 414
    HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415
    HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = 416
    HTTP_417_EXPECTATION_FAILED = 417
    HTTP_418_IM_A_TEAPOT = 418
    HTTP_422_UNPROCESSABLE_ENTITY = 422
    HTTP_423_LOCKED = 423
    HTTP_424_FAILED_DEPENDENCY = 424
    HTTP_426_UPGRADE_REQUIRED = 426
    HTTP_428_PRECONDITION_REQUIRED = 428
    HTTP_429_TOO_MANY_REQUESTS = 429
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451
    HTTP_499_CANCELLED_ERROR = 499
    HTTP_500_INTERNAL_SERVER_ERROR = 500
    HTTP_501_NOT_IMPLEMENTED = 501
    HTTP_502_BAD_GATEWAY = 502
    HTTP_503_SERVICE_UNAVAILABLE = 503
    HTTP_504_GATEWAY_TIMEOUT = 504
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505
    HTTP_506_VARIANT_ALSO_NEGOTIATES = 506
    HTTP_507_INSUFFICIENT_STORAGE = 507
    HTTP_508_LOOP_DETECTED = 508
    HTTP_509_BANDWIDTH_LIMIT_EXCEEDED = 509
    HTTP_510_NOT_EXTENDED = 510
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511

# 定义一个异常类，继承Exception，


class APIException(Exception):
    status = 'INTERNAL'
    StatusCode = 400
    details = []
    message = {
        "errors": {
            "status": status,
            "details": details
        }
    }
    debug = None

    # 初始化对象接收异常参数，传字典格式进来
    def __init__(self, detail=None):
        if not detail:
            return
        self.details = []
        if isinstance(detail, list):
            self.details.extend(detail)
        else:
            self.details.append(detail)

    @property
    def errors(self):  # 组装返回格式
        self.message["errors"]['status'] = self.status
        self.message["errors"]['details'] = self.details
        self.message["errors"]['StatusCode'] = self.StatusCode
        if self.debug:
            self.message["errors"]["debug"] = self.debug
        return self.message

# 下面是定义每个异常的错误类型


class InvalidArgumentError(APIException):
    status = 'INVALID_ARGUMENT'
    StatusCode = StatusCode.HTTP_404_NOT_FOUND


class FailedPreconditionError(APIException):
    status = 'FAILED_PRECONDITION'
    StatusCode = StatusCode.HTTP_400_BAD_REQUEST


class OutOfRangeError(APIException):
    status = 'OUT_OF_RANGE'
    StatusCode = StatusCode.HTTP_400_BAD_REQUEST


class UnauthenticatedError(APIException):
    status = 'UNAUTHENTICATED'
    StatusCode = StatusCode.HTTP_401_UNAUTHORIZED


class PermissionDeniedError(APIException):
    status = 'PERMISSION_DENIED'
    StatusCode = StatusCode.HTTP_403_FORBIDDEN


class NotFoundError(APIException):
    status = 'NOT_FOUND'
    StatusCode = StatusCode.HTTP_404_NOT_FOUND


class MethodNotAllowedError(APIException):
    status = 'METHOD_NOT_ALLOWED'
    StatusCode = StatusCode.HTTP_405_METHOD_NOT_ALLOWED


class AbortedError(APIException):
    status = 'ABORTED'
    StatusCode = StatusCode.HTTP_409_CONFLICT


class AlreadyExistsError(APIException):
    status = 'ALREADY_EXISTS'
    StatusCode = StatusCode.HTTP_409_CONFLICT


class ResourceExhaustedError(APIException):
    status = 'RESOURCE_EXHAUSTED'
    StatusCode = StatusCode.HTTP_429_TOO_MANY_REQUESTS


class CancelledError(APIException):
    status = 'CANCELLED'
    StatusCode = StatusCode.HTTP_499_CANCELLED_ERROR


class DataLossError(APIException):
    status = 'DATA_LOSS'
    StatusCode = StatusCode.HTTP_500_INTERNAL_SERVER_ERROR


class UnknownError(APIException):
    status = 'UNKNOWN'
    StatusCode = StatusCode.HTTP_500_INTERNAL_SERVER_ERROR


class InternalError(APIException):
    status = 'INTERNAL'
    StatusCode = StatusCode.HTTP_500_INTERNAL_SERVER_ERROR


class NotImplementError(APIException):
    status = 'NOT_IMPLEMENTED'
    StatusCode = StatusCode.HTTP_501_NOT_IMPLEMENTED


class UnavailableError(APIException):
    status = 'UNAVAILABLE'
    StatusCode = StatusCode.HTTP_503_SERVICE_UNAVAILABLE


class DeadlineExceededError(APIException):
    status = 'DEADLINE_EXCEEDED'
    StatusCode = StatusCode.HTTP_504_GATEWAY_TIMEOUT

# 定义一个装饰器，处理异常


def return_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            return e.errors
    return wrapper

# 给函数做装饰


@return_error
def func1(error=True):
    if error:
        raise InvalidArgumentError({"field": "index", "message": "模拟抛出异常异常内容"})
    return '无异常'

# # 调用被装饰的函数
# @app.route('/')
# def index():
#     res = func1()
#     return jsonify(res)


# if __name__ == '__main__':
#     app.run(host="0.0.0.0", debug=True)
#
