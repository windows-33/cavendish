package com.windows33.cavendish.domain.part.computer_case.entity;

import com.windows33.cavendish.global.entity.PartCommonEntity;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.experimental.SuperBuilder;

import javax.persistence.*;

@Getter
@SuperBuilder
@NoArgsConstructor
@Table(name = "`case`")
@Entity
public class ComputerCase extends PartCommonEntity {

    private String category;

    private String size;

    private String powerIncluded;

    private String powerSupport;

    private Integer boardSupport;

    @Column(name = "bay_133")
    private Integer bay_133;

    @Column(name = "bay_89")
    private Integer bay_89;

    @Column(name = "bay_64")
    private Integer bay_64;

    private Integer pciHorizontal;

    private Integer pciVertical;

    private Integer coolingFan;

    private Integer ledFan;

    private String frontType;

    private String sideOpen;

    private String sideType;

    private String backVent;

    private String frontVent;

    private String topVent;

    private String bottomVent;

    private Integer externalPort;

    private Float width;

    private Float height;

    private Float depth;

    private Integer gpuSize;

    private Integer cpuCoolerSize;

    private Integer powerSize;

    private Integer liquidCooler;

    private Integer radiatorTop;

    private Integer radiatorFront;

    private Integer radiatorRear;

    private Integer radiatorSide;

    private Integer feature;

    private String ledColor;

}
