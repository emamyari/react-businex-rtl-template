import React, { useState } from 'react';
import FormInput from "../../components/UI/Input";

const From = () => {
    const [stateName,SetStateName]=useState("")
    const [stateFamily,SetStateFamily]=useState("")
    const [stateTel,SetStateTel]=useState("")
    const [stateEmail,SetStateEmail]=useState("")
    const [stateText,SetStateText]=useState("")
    const [stateFile,SetStateFile]=useState("")
 

    function step1(){

        const reader = new FileReader();
        reader.onloadend = () => {
           
           sendToServer(reader.result)
            
        };
        reader.readAsDataURL(stateFile);
    }



    function sendToServer(file){
             var myHeaders = new Headers();
             myHeaders.append("Content-Type", "application/json");
            
            var raw = JSON.stringify({
                "Name": stateName,
                "Family": stateFamily,
                "Email": stateEmail,
                "Tel": stateTel,
                "Text": stateText,
                "File": file
            });
    
            var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            };
    
            fetch("http://192.168.1.3:7000/insertContact/", requestOptions)
            .then(response => response.text())
            .then(result => console.log(result))
            .catch(error => console.log('error', error));
    }


    return (
        <div className="contact-form-wrap">
                 <div className="row">
                    <div className="col-md-6">
                        <div className="single-input-item">
                            <label>
                                <input onChange={e=>SetStateName(e.target.value)} placeholder='محمود    ' />
                            </label>
                        </div>
                    </div>

                    <div className="col-md-6">
                        <div className="single-input-item">
                            <label>
                                <input  onChange={e=>SetStateFamily(e.target.value)} placeholder='احمدی نژاد ' />
                            </label>
                        </div>

                    </div>

                    <div className="col-md-6">
                        <div className="single-input-item">
                            <label>
                                <input onChange={e=>SetStateTel(e.target.value)} placeholder='09123420142' />
                            </label>
                        </div>
                    </div>

                    <div className="col-md-6">
                        <div className="single-input-item">
                            <label>
                                <input onChange={e=>SetStateEmail(e.target.value)} placeholder='emamyari@yahoo.com' />
                            </label>
                        </div>
                    </div>

                    <div className="col-md-6">
                        <div className="single-input-item">
                            <label>
                                <input type='file' onChange={e=>SetStateFile(e.target.files[0])}  />
                            </label>
                        </div>
                    </div>


                    <div className="col-12">
                        <div className="single-input-item">
                            <label>
                                <textarea onChange={e=>SetStateText(e.target.value)} cols="30" rows="7" placeholder='متن نامه ' required />
                            </label>
                        </div>

                        <div className="single-input-item">
                            <label>
                                <button onClick={step1} className={`btn-outline  `}>ارسال پیام</button>

                            </label>
                        </div>

                        <div className="form-message" />
                    </div>
                </div>
         </div>
    );
};

export default From;
