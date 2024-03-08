import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function SolutionTable({ solutions }) {
  return (
    <TableContainer component={Paper} sx={{
      // General styles
      maxWidth: 650,
      margin: '0 auto',
      // Styles for light mode
      '@media (prefers-color-scheme: dark)': {
        bgcolor: '#ffffff', // Background color for the table container
        color: '#213547', // Text color
        // Further customization can go here
      }
    }}>
      <Table aria-label="solutions table">
        <TableHead>
          <TableRow sx={{
            '@media (prefers-color-scheme: dark)': {
              // Styles for the table header in light mode
              // Example: changing the background color of the header row
              bgcolor: '#1a1a1a',
              '& .MuiTableCell-head': {
                color: 'white', // Text color for the header cells
                fontSize: 'larger'
              },
            },
          }}>
            <TableCell>Title</TableCell>
            <TableCell align="right">Difficulty</TableCell>
            <TableCell align="right">Companies</TableCell>
            <TableCell align="right">Programming Languages</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {solutions.map((solution) => (
            <TableRow
              key={solution.title}
              sx={{
                '&:last-child td, &:last-child th': { border: 0 },
                '@media (prefers-color-scheme: dark)': {
                  bgcolor: '#222',
                  '& .MuiTableCell-head': {
                  },
                },
              }}
            >
              <TableCell component="th" scope="row" sx={{
                '@media (prefers-color-scheme: dark)': {
                  color: 'white',
                }
              }}>
                {solution.title}
              </TableCell>
              <TableCell align="right" sx={{
                '@media (prefers-color-scheme: dark)': {
                  color: 'white',
                }
              }}
              >{solution.difficulty}</TableCell>
              <TableCell align="right" sx={{
                '@media (prefers-color-scheme: dark)': {
                  color: 'white',
                }
              }}>
                {solution.companies.map(company => company.name).join(", ")}
              </TableCell>
              <TableCell align="right" sx={{
                '@media (prefers-color-scheme: dark)': {
                  color: 'white',
                }
              }}>
                {solution.programming_languages.map(language => language.name).join(", ")}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

export default SolutionTable;
