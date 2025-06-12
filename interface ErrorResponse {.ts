interface ErrorResponse {
  code: number;      // 错误状态码
  message: string;   // 错误提示信息
  errors?: any;      // 详细错误信息（可选）
}

function error(message: string, code: number = 400, errors?: any): ErrorResponse {
  return {
    code,
    message,
    errors
  };
}