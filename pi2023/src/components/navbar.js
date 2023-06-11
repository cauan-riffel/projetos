import React from "react";
import $ from 'jquery';

export default class Navbar extends React.Component {
	constructor(props){
		super(props);
		this.itemNames=props.linkNames;
		this.height=Number(props.height);
		this.destiny=props.destiny;
		this.margin=Number(props.margin);
	}

	getMargin(height,elementHeight){
		return (elementHeight||this.height)/2 - height/2;
	}

	getPercent(percentage){
		return this.height*percentage;
	}

	moveTo(destiny){ //! precisa implementar
		if(typeof(Number(destiny))=='number'){
			window.scrollTo({
				top:destiny,
				behavior:'smooth'
			})
		}else if(typeof(destiny)=='string'){
			let top=$(`#${destiny}`).offset();
			console.log(top);
			window.scrollTo({top,,behavior:'smooth'});
		}
	}

	render(){
		const divStyle={
			position:"fixed", width:"100%",
			height:this.height, backgroundColor:'whitesmoke'
		}

		const imgStyle={
			display: "inline-block", height: this.getPercent(0.65),
			marginTop: this.getMargin(this.getPercent(0.65)), float: "left",
			marginLeft:this.margin
		}

		const navStyle={
			listStyle:"none", display:"inline-block",
			height:this.getPercent(0.65), marginTop:this.getMargin(this.getPercent(0.65)),
			float:"right", marginRight:this.margin
		}

		const listStyle={
			display:"inline-block", marginRight:this.getPercent(0.5),
			marginTop:this.getMargin(this.getPercent(0.3),this.getPercent(0.65))
		}
		const items=this.itemNames.map((content,index)=>(
			<li key={index} onClick={this.moveTo(this.destiny[index])} style={listStyle}>{content}</li>
		))

		return(
			<>
				<div style={divStyle}>
					<img style={imgStyle} src="/logo.png" />
					<nav style={navStyle}>{items}</nav>
				</div>
				<div style={{height:this.height}}></div>
			</>
		);
	}
}
