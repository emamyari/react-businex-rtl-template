import React, { useState } from 'react';
import FormInput from "../../components/UI/Input";

const From = () => {
    const [stateName,SetStateName]=useState("")
    const [stateFamily,SetStateFamily]=useState("")
    const [stateTel,SetStateTel]=useState("")
    const [stateEmail,SetStateEmail]=useState("")
    const [stateText,SetStateText]=useState("")

    function sendToServer(){
        console.log(stateName)
        console.log(stateFamily)
        console.log(stateTel)
        console.log(stateEmail)
        console.log(stateText)
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

                    <div className="col-12">
                        <div className="single-input-item">
                            <label>
                                <textarea onChange={e=>SetStateText(e.target.value)} cols="30" rows="7" placeholder='متن نامه ' required />
                            </label>
                        </div>

                        <div className="single-input-item">
                            <label>
                                <button onClick={sendToServer} className={`btn-outline  `}>ارسال پیام</button>

                            </label>
                        </div>

                        <div className="form-message" />
                    </div>
                </div>
         </div>
    );
};

export default From;
