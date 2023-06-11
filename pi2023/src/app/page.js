'use client'
import React from "react";
import Navbar from "@/components/navbar";
import MainContent from "@/components/content";


export default class Home extends React.Component{
	constructor(props){
		super(props);
		this.margin=85;
	}
	render(){
		return (
			<div className="root">
				<Navbar
					margin={this.margin}
					height={65}
					destiny={['ContentId',75,84]}
					linkNames={['Página Inicial','Sobre','Contato']}
				/>
				<MainContent
					type='centered'
					id='content1'

					title='Equilíbrio entre vida pessoal e profissional.					'
					subTitle='Amostra de Citação. Lorem ipsum dolor sit amet, consectetur adipiscing elit nullam nunc justo sagittis suscipit ultrices.!!!'

					height={600}
				/>
				<MainContent
					type='reversed'
					id='content2'

					title='QUIZ'
					subTitle='Sample text. Click to select the text box. Click again or double click to start editing the text'
					img='/whitenone.png'

					height={420}
				/>
			</div>
		);
	}

}
