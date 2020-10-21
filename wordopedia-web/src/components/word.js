import React, {useEffect, useState} from 'react';
import axios from 'axios';

function Word(){
    const [wrd, setWrd] = useState('');
    const [last_wrd, setLastWrd] = useState(4760);
    const [l, setL] = useState('')
    var r = '';
    var flag = false;
    useEffect(() => {
        getCurrentUser()
    }, [])  
    const clickContinue = () => {
        getWord(last_wrd)
        flag = true;
        console.log("cc", last_wrd)
    }
    const getWord = (ep) => {
        axios.get(`http://localhost:8000/api/words/${ep}`, {
            headers: {
                'accept': 'application/json'
            }
        }).then(resp => {
            r = resp.data;
            setWrd(r)
            console.log("getWord")
        })
    }
    const next = () => {
        if(last_wrd <= 9518 && last_wrd >= 4760){
            var ep = last_wrd + 1
            getWord(ep)
            setLastWrd(ep)
            updatecurrentUser()
            console.log("next")

        }
    }
    const prev = () => {
        if (last_wrd >= 4760 && last_wrd <= 9518){
            var ep = last_wrd - 1
            getWord(ep)
            setLastWrd(ep)
            updatecurrentUser()
            console.log("prev")
        }  
    }

    const getCurrentUser = () => {
        axios.get(`http://localhost:8000/accounts/api/user/current`, {
            headers: {
                'accept': 'application/json'
            }
        }).then(resp => {
            var r = resp.data;
            console.log("r", r)
            setL(resp.data)
            setLastWrd(r.last_visited_word)
            console.log("getCurrentUser")
            
        })
    }
    const updatecurrentUser = () => {
        var item  = {
            "last_visited_word": last_wrd
        }
        axios.put(`http://localhost:8000/accounts/api/user/edit/${l.id}`, item).then(res => console.log("UpdateCurrentUSer", item))
    }
    return (
        <div className="container">
                    <br/>
                    {clickContinue()}
                    <div className="card" style={{width: 18 + 'rem'}}>
                        <div className="card-body">
                            <h5 className="card-title">{ wrd.word }</h5>
                            <p className="card-text">{ wrd.meaning }</p>
                            <br/>
                            <div className="row">
                                <div className="col-3">
                                    {last_wrd > 4760 && <button className = "btn btn-primary" onClick={prev}>prev</button>}
                                </div>
                                <div className="col-3">
                                    {last_wrd < 9518 && <button className = "btn btn-primary" onClick={next}>next</button>}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
    )
}



export default Word;
