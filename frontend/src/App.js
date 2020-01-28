import React, { Component } from 'react';

class App extends Component {
  state = {
    todos: []
  };
/* 
   This is where the magic happens
*/
  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/display_data/'); // fetching the data from api, before the page loaded
      const todos = await res.json();
      this.setState({
        todos
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.country_name}</h1>
            <span>{item.country_code}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;