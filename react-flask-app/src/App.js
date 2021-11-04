import logo from './logo.svg';
import './App.css';
import Header from './components/Header.js'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Header contact={{username: "XYZ"}}/>
        
      </header>
    </div>
  );
}

export default App;
