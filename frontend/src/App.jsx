// frontend/src/App.jsx
import { useAuth } from "./context/AuthContext";
import Login from "./components/Login";
import Bookmarks from "./components/Bookmarks";
import "./App.css";

function App() {
  const { token } = useAuth();

  return (
    <div className="App">
      <header className="App-header">
        <h1>LinkVault</h1>
      </header>
      <main>{token ? <Bookmarks /> : <Login />}</main>
    </div>
  );
}
export default App;
