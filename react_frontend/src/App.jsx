import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage/HomePage'
import SolutionsPage from './pages/Solutions/SolutionsPage';
// import About from './components/About'; //TODO
import NotFound from './pages/NotFound/NotFoundPage'; //TODO
import './App.css'


function App() {
  return (
    
    <Router>
    <div className="App">
      {/* Define your routes here */}
      <Routes>
        <Route path="/" element={<HomePage />} />
        {/* <Route path="/about" element={<About />} /> */}
        <Route path="/solutions" element={ <SolutionsPage/> } />
        {/* Add a catch-all route for 404 pages */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  </Router>
    
  )
}

export default App
