import React from 'react';
import parse from "html-react-parser";
//import aboutData from "../../../data/About/home-two";
import aboutThumb from '../../../assets/img/about-2-bg.jpg'
import {Link} from "react-router-dom";
import { useEffect,useState } from 'react';


const About = () => {

   const [aboutData,setAboutData]=useState(
        {
        "title": "",
        "heading": "",
        "since": "",
        "text": "",
        "btnText": " ",
        "btnLink": "",
        "thumb": "fun-fact-bg.jpg"
      }
      )

      useEffect(() => {
        fetch("http://192.168.1.3:7000/getAbout/")
        .then(response => response.json())
        .then(result => setAboutData(result))
        .catch(error => console.log('error', error));
      },[]);




    return (
        <div className="home-two-about-area" style={{backgroundImage:`url(${aboutThumb})`}}>
            <div className="container">
                <div className="row align-items-center">
                    <div className="col-12 d-lg-none">
                        <figure className="about-thumb">
                            <img src={require('../../../assets/img/' + aboutData.thumb)} alt="Businex-About"/>
                        </figure>
                    </div>
 
                    <div className="col-lg-6">
                        <div className="about-content about-content--2">
                            <h2>{parse(aboutData.heading)}</h2>
                            <span className="about-since">{aboutData.since}</span>
                            <p>{parse(aboutData.text)}</p>
                            <Link to={`${process.env.PUBLIC_URL + aboutData.btnLink}`} className="btn-about">{aboutData.btnText} <i className="fa fa-angle-double-left"/></Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default About;
