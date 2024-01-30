import Allrestaurants from "./Allrestaurants";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <main>
        <BrowserRouter>
          <Routes>
            <Route path='/' element={<Allrestaurants />} />
          </Routes>
        </BrowserRouter>
      </main>
    </div>
  );
}

export default App;
