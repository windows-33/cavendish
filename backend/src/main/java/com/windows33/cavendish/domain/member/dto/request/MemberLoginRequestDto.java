package com.windows33.cavendish.domain.member.dto.request;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class MemberLoginRequestDto {

    private String loginId;
    private String password;

}
