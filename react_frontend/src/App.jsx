import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage/HomePage'
import SolutionsPage from './pages/Solutions/SolutionsPage';
import About from './pages/About/AboutPage';
import NotFound from './pages/NotFound/NotFoundPage';
import './App.css'


function App() {
  return (
    
    <Router>
    <div className="App">
      
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<About />} />
        <Route path="/solutions" element={ <SolutionsPage/> } />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  </Router>
    
  )
}

export default App
