import React, { Component } from 'react';

class App extends Component {
  state = {
    wdi_data: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/display_data/'); // fetching the data from api, before the page loaded
      const wdi_data = await res.json();
      this.setState({
        wdi_data
      });
    } catch (e) {
      console.log(e);
    }
  }

  renderTableData() {
    return this.state.wdi_data.map((listValue, index) => {
      const { id, country_name, country_code, indicator_name, indicator_code, y_1960, y_1961, y_1962, y_1963, y_1964, y_1965, y_1966, y_1967, y_1968, y_1969, y_1970, y_1971, y_1972, y_1973, y_1974, y_1975, y_1976, y_1977, y_1978, y_1979, y_1980, y_1981, y_1982, y_1983, y_1984, y_1985, y_1986, y_1987, y_1988, y_1989, y_1990, y_1991, y_1992, y_1993, y_1994, y_1995, y_1996, y_1997, y_1998, y_1999, y_2000, y_2001, y_2002, y_2003, y_2004, y_2005, y_2006, y_2007, y_2008, y_2009, y_2010, y_2011, y_2012, y_2013, y_2014, y_2015, y_2016, y_2017, y_2018, y_2019  } = listValue
      return (
        <tr key={id}>
          <td>{id}</td>
          <td>{country_name}</td> 
          <td>{country_code}</td> 
          <td>{indicator_name}</td> 
          <td>{indicator_code}</td>          
          <td>{y_1960}</td>
          <td>{y_1961}</td>
          <td>{y_1962}</td>
          <td>{y_1963}</td>
          <td>{y_1964}</td>
          <td>{y_1965}</td>
          <td>{y_1966}</td>
          <td>{y_1967}</td>
          <td>{y_1968}</td>
          <td>{y_1969}</td>
          <td>{y_1970}</td>
          <td>{y_1971}</td>
          <td>{y_1972}</td>
          <td>{y_1973}</td>
          <td>{y_1974}</td>
          <td>{y_1975}</td>
          <td>{y_1976}</td>
          <td>{y_1977}</td>
          <td>{y_1978}</td>
          <td>{y_1979}</td>
          <td>{y_1980}</td>
          <td>{y_1981}</td>
          <td>{y_1982}</td>
          <td>{y_1983}</td>
          <td>{y_1984}</td>
          <td>{y_1985}</td>
          <td>{y_1986}</td>
          <td>{y_1987}</td>
          <td>{y_1988}</td>
          <td>{y_1989}</td>
          <td>{y_1990}</td>
          <td>{y_1991}</td>
          <td>{y_1992}</td>
          <td>{y_1993}</td>
          <td>{y_1994}</td>
          <td>{y_1995}</td>
          <td>{y_1996}</td>
          <td>{y_1997}</td>
          <td>{y_1998}</td>
          <td>{y_1999}</td>
          <td>{y_2000}</td>
          <td>{y_2001}</td>
          <td>{y_2002}</td>
          <td>{y_2003}</td>
          <td>{y_2004}</td>
          <td>{y_2005}</td>
          <td>{y_2006}</td>
          <td>{y_2007}</td>
          <td>{y_2008}</td>
          <td>{y_2009}</td>
          <td>{y_2010}</td>
          <td>{y_2011}</td>
          <td>{y_2012}</td>
          <td>{y_2013}</td>
          <td>{y_2014}</td>
          <td>{y_2015}</td>
          <td>{y_2016}</td>
          <td>{y_2017}</td>
          <td>{y_2018}</td>
          <td>{y_2019}</td>
        </tr>
      )
    })
  }

  renderTableHeader() {
    var s = this.state.wdi_data[1]
    var keys = [];
    for(var k in s) keys.push(k);
    return keys.map((key, index) => {
      console.log(key)
      if (key != "data_type") {
        return <th key={index}>{key.toUpperCase()}</th>
      }
    })
 }

  render() {
    return (
      <div>
        {/* {this.state.wdi_data.map(item => (
          <div key={item.id}>
            <h1>{item.country_name}</h1>
            <span>{item.country_code}</span>
          </div>
        ))} */}
      
        {/* <h2>Showing <strong>{this.state.wdi_data.length} items</strong></h2>
        <table>
        <tr>
        {this.state.wdi_data.map(( listValue, index ) =>
            <tr key={index}>
            <td>{listValue.country_name}</td>
            <td>{listValue.country_code}</td>
            <td>{listValue.y_1960}</td>
          </tr>
          )}
        </tr>>
          <tr>
            {this.state.wdi_data.map(item => 
              <th>{item.country_name}</th>
            )}
          </tr>
        </table> */}
        <h1 id = 'title'>World Development Indicators</h1>
        <table id='wdi-data'>
          <tbody>
            <tr>{this.renderTableHeader()}</tr>
            {this.renderTableData()}
          </tbody>
        </table>
      </div>
    );
  }
}

export default App;