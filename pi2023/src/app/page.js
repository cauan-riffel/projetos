'use client'
import React from "react";
import Navbar from "@/components/navbar";
import MainContent from "@/components/content";


export default class Home extends React.Component{
	setMargin(){
		let width=screen.availWidth;
		if(width>888&&this.state.navBarMargin!=85){
			this.setState({
				navBarMargin: 85,
				navBarHeight: 65,

				contentHeight:600,
			});
		}else if(width>400&&this.state.navBarMargin!=60){
			this.setState({
				navBarMargin: 85,
				navBarHeight: 65,

				contentHeight:600,
			});
		}
	}

	constructor(props){
		super(props);
		this.state={
			navBarMargin: 85,
			navBarHeight: 65,

			contentHeight:725,

		}
	}
	render(){
		return (
			<div className="root">
				<Navbar
					margin={this.state.navBarMargin}
					height={this.state.navBarHeight}
					destiny={['ContentId','content2',400]}
					linkNames={['Página Inicial','Sobre','Contato']}
				/>
				<MainContent
					type='centered'
					id='content1'

					title='Equilíbrio entre vida pessoal e profissional.					'
					subTitle='Amostra de Citação. Lorem ipsum dolor sit amet, consectetur adipiscing elit nullam nunc justo sagittis suscipit ultrices.!!!'

					height={this.state.contentHeight}
				/>
				<MainContent
					type='reversed'
					id='content2'

					title='QUIZ'
					subTitle='Sample text. Click to select the text box. Click again or double click to start editing the text'
					img='/whitenone.png'

					height={this.state.contentHeight}
				/>
				<MainContent
					type='centered'
					id='content1'

					title='Equilíbrio entre vida pessoal e profissional.					'
					subTitle='Amostra de Citação. Lorem ipsum dolor sit amet, consectetur adipiscing elit nullam nunc justo sagittis suscipit ultrices.!!!'

					height={this.state.contentHeight}
				/>
			</div>
		);
	}
}
