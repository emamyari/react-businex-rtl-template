import React, { useEffect, useState } from 'react';
import SectionTitle from '../UI/SectionTitle'
import ServiceItem from  './ServiceItem'

import serviceTopBg from '../../assets/img/service/service-bg.jpg'

function Services({classes}) {

    const [sData,setSData]=useState([])

    useEffect(() => {
        fetch("http://192.168.1.3:7000/getServices/")
        .then(response => response.json())
        .then(result => setSData(result))
        .catch(error => console.log('error', error));
      },[]);




    return (
        <div className={`service-area-wrapper ${classes}`}>
            <div className="service-area-top" style={{backgroundImage: `url("${serviceTopBg}")`}}>
                <div className="container">
                    <div className="row">
                        <div className="col-lg-6 col-xl-5 m-auto text-center">
                            <SectionTitle variant="light" title="خدمات ما" heading="ما راه پیشرفت شما را هموار می کنیم" />
                        </div>
                    </div>
                </div>
            </div>

            <div className="service-content-area">
                <div className="container">
                    <div className="row mtn-30">
                        {
                            sData.map(service=>(
                                <ServiceItem key={service.id} id={service.id} title={service.title} text={service.shortDesc} thumb={service.thumb}/>
                            ))
                        }
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Services;
