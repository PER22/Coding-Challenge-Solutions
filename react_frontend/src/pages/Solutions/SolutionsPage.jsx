import React, { useState, useEffect } from 'react';
import { Typography } from '@mui/material';
import { fetchSolutions } from '../../utilities/solutions-service';
import { fetchCompanies } from '../../utilities/companies-service'
import SolutionTable from './components/SolutionTable';
import SolutionFilterControls from './components/SolutionFilterControls'
import './SolutionsPage.css'


const SolutionsPage = () => {
  const [solutions, setSolutions] = useState([]);
  const [filters, setFilters] = useState({
    language: null,
    companies: [],
    difficulty: null
  });
  const [companies, setCompanies] = useState([]);
  
  //Companies
  useEffect(() => {
    async function getCompanies() {
      const response = await fetchCompanies();
      setCompanies(response);
    }
    getCompanies();
  }, []);


  //Fetch upon filter change
  useEffect(() => {
    async function getSolutions(filters) {
      const response = await fetchSolutions(filters);
      setSolutions(response);
    }
    getSolutions(filters);
  }, [filters]);

  return (
    <div id="solutions-page">
      <div id="filters-section">
        <Typography>Filters</Typography>
        <SolutionFilterControls filters={filters} setFilters={setFilters} companies={companies}/>
      </div>
      <div className="solutions-section">
        <Typography>Solutions</Typography>
        <SolutionTable solutions={solutions}></SolutionTable>
      </div>
    </div>
  );
};

export default SolutionsPage;
