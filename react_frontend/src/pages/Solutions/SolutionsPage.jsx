import React, { useState, useEffect } from 'react';
import {fetchSolutions}  from '../../utilities/solutions-service'; 
import SolutionTable from './components/SolutionTable';
import SolutionFilterControls from './components/SolutionFilterControls'


const SolutionsPage = () => {
    const [solutions, setSolutions] = useState([]);
    const [filters, setFilters] = useState({
        language: null,
        companies: [],
        difficulty: null
    });    

    //Filters
    useEffect(() => {
      async function getSolutions(filters) {
        const response = await fetchSolutions(filters);
        setSolutions(response);
      }
      getSolutions(filters);
    }, [filters]);
  
    return (
      <div>
        <h1>Filters</h1>
        <SolutionFilterControls filters={filters} setFilters={setFilters}/>
        <h1>Solutions</h1>
        <SolutionTable solutions={solutions} ></SolutionTable>
      </div>
    );
};

export default SolutionsPage;
