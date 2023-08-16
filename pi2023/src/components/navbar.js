import React from "react";
import './nav.css';

export default class NavBar extends React.Component{
	constructor(props){
		super(props);
		this.height=Number(props.height);
		this.margin=Number(props.margin);
		this.itemNames=props.linkNames;
		this.destiny=props.destiny;

		//optional
		this.color=props.color||'whitesmoke'
	}
	render(){
		if(screen.availWidth>700){
			return (
				<DesktopNav
					margin={this.margin}
					height={this.height}
					destiny={this.destiny}
					linkNames={this.itemNames}
					color={this.color}
				/>);
		}
	}
}


class DesktopNav extends React.Component {
	constructor(props){
		super(props);
		this.height=Number(props.height);
		this.margin=Number(props.margin);

		this.itemNames=props.linkNames;
		this.destiny=props.destiny;

		this.color=props.color;
	}

	getMargin(height,elementHeight){
		return (elementHeight||this.height)/2 - height/2;
	}

	getPercent(percentage){
		return this.height*percentage;
	}

	moveTo(destiny){ //! precisa implementar
		if(document.getElementById(destiny)==null){
			window.scrollTo({top:destiny,behavior:'smooth'});
		}else if(typeof(destiny)=='string'){
			let top=document.getElementById(destiny).offsetTop-document.getElementById('navBar').offsetHeight;
			window.scrollTo({top,behavior:'smooth'});
		}
	}

	render(){
		const divStyle={
			height:this.height, backgroundColor:this.color
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
			<li key={index} className="in" onClick={()=>this.moveTo(this.destiny[index]||0)} style={listStyle}>{content}</li>
		))

		return(
			<>
				<div id="navBar" style={divStyle}>
					<img className="in" onClick={()=>this.moveTo(0)} style={imgStyle} src="/logo.png" />
					<nav style={navStyle}>{items}</nav>
				</div>
				<div style={{height:this.height}}></div>
			</>
		);
	}
}
