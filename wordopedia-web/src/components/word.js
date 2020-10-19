import React, {useEffect, useState} from 'react';
import axios from 'axios';

function Word(){
    const [words_list, setWords_list] = useState([]);
    const [wrd, setWrd] = useState('');
    const [endpoint, setEndpoint] = useState(4760);
    var r = '';
    useEffect(() => {
        getWord(endpoint)
    }, [])  
    function getWord(ep){
        axios.get(`http://localhost:8000/api/words/${ep}`, {
            headers: {
                'accept': 'application/json'
            }
        }).then(resp => {
            r = resp.data;
            setWrd(r)
            console.log(wrd)
        })
    }
    function next(){
        if(endpoint <= 9518 && endpoint >= 4760){
            var ep = endpoint + 1
            setEndpoint(ep)
            console.log('next', ep)
            getWord(ep)
        }
    }
    function prev(){
        if (endpoint >= 4760 && endpoint <= 9518){
            var ep = endpoint - 1
            setEndpoint(ep)
            console.log('prev', ep)
            getWord(ep)
        }  
    }
    
    return (
        <div className="container">
            <br/>
            <div className="card" style={{width: 18 + 'rem'}}>
                <div className="card-body">
                    <h5 className="card-title">{ wrd.word }</h5>
                    <p className="card-text">{ wrd.meaning }</p>
                    <br/>
                    {getWord}
                    <div className="row">
                        <div className="col-3">
                            {endpoint > 4760 && <button className = "btn btn-primary" onClick={prev}>prev</button>}
                        </div>
                        <div className="col-3">
                            {endpoint < 9518 && <button className = "btn btn-primary" onClick={next}>next</button>}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )

}

export default Word;
