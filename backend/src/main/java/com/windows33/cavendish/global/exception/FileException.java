package com.windows33.cavendish.global.exception;

import org.apache.commons.lang3.StringUtils;

public class FileException extends ServiceRuntimeException{

    static final String MESSAGE_KEY = "ERROR.FILE";

    public FileException(Class clazz, Object... values) {
        super(MESSAGE_KEY, clazz.getSimpleName(), (values != null && values.length > 0) ? StringUtils.join(values, ",") : "");
    }

}