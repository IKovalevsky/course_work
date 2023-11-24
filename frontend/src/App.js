import axios from 'axios';
import './App.css';
import React from 'react'

class App extends React.Component{
  state = {details: [],}

  componentDidMount(){
    let data;
    axios.get('http://localhost:8000').then(res => {
      data = res.data;
      this.setState({
        details: data
      })
    })
    .catch(err => {
      console.log(err);
    })
  }
  render(){
    return(
      <div>
        <header> Данные из Django</header>
      </div>
    )
  }
}

export default App;
